from PIL import Image, ImageDraw
from math import sqrt
from find_anomal import get_data_anomauls


width = 40
height = 30


def fill_graph(matrix, used_cells):
    for it in matrix:
        x, y = it
        for i in range(-1, 2):
            for j in range(-1, 2):
                if i == j == 0:
                    continue
                if (x + i, y + j) in used_cells:
                    matrix[it].append([x + i, y + j, 10 ** 9])
                    continue
                if 0 <= x + i < width and 0 <= y + j < height:
                    matrix[it].append([x + i, y + j, sqrt(i ** 2 + j ** 2)])


def draw_anomalous(arr, s, f):
    matrix = {(i, j): [] for i in range(width) for j in range(height)}
    used_cells = set()

    im0 = Image.open("makets_predprof/map.png").convert("RGBA")
    im = Image.new("RGBA", im0.size, (255, 255, 255, 0))
    drawer = ImageDraw.Draw(im)
    for anom in arr:
        r = sqrt(2500 * anom[2] / 2)
        x1 = anom[0] * 50 - r
        y1 = anom[1] * 50 - r
        x2 = anom[0] * 50 + r
        y2 = anom[1] * 50 + r
        drawer.ellipse((
            (x1, y1),
            (x2, y2)),
            fill=(230, 0, 0, 120))
        for i in range(width):
            for j in range(height):
                if x1 <= i * 50 <= x2 and y1 <= j * 50 <= y2:
                    used_cells.add((i, j))
    for anom in arr:
        drawer.ellipse((
            (anom[0] * 50 - 25, anom[1] * 50 - 25),
            (anom[0] * 50 + 25, anom[1] * 50 + 25)), fill=(0, 0, 250, 180))
    fill_graph(matrix, used_cells)
    path_ = deixtra(matrix, s, f)
    for i in range(1, len(path_)):
        drawer.line((path_[i - 1][0] * 50, path_[i - 1][1] * 50,
                     path_[i][0] * 50, path_[i][1] * 50), fill=(255, 255, 255), width=3)
    drawer.ellipse((
        (path_[0][0] * 50 - 10, path_[0][1] * 50 - 10),
        (path_[0][0] * 50 + 10, path_[0][1] * 50 + 10)), fill=(200, 200, 0))
    drawer.text(
        (path_[0][0] * 50, path_[0][1] * 50),
        'A', font_size=80
    )
    drawer.ellipse((
        (path_[-1][0] * 50 - 10, path_[-1][1] * 50 - 10),
        (path_[-1][0] * 50 + 10, path_[-1][1] * 50 + 10)), fill=(200, 200, 0))
    drawer.text(
        (path_[-1][0] * 50, path_[-1][1] * 50),
        'B', font_size=80
    )
    out = Image.alpha_composite(im0, im)
    out.save("makets_predprof/map2.png")


def deixtra(matrix, s, f):
    used = {(i, j): 0 for i in range(width) for j in range(height)}
    dist = {(i, j): 10 ** 9 for i in range(width) for j in range(height)}
    par = {(i, j): (-1, -1) for i in range(width) for j in range(height)}
    dist[s] = 0
    now = s
    for i in range(width):
        for j in range(height):
            used[now] = 1
            for nxt in matrix[now]:
                if dist[(nxt[0], nxt[1])] > nxt[2] + dist[now]:
                    par[(nxt[0], nxt[1])] = now
                    dist[(nxt[0], nxt[1])] = nxt[2] + dist[now]
            mn_ind = 10**9
            ind = (-1, -1)
            for i1 in range(width):
                for j1 in range(height):
                    if used[(i1, j1)] == 0 and dist[(i1, j1)] < mn_ind:
                        ind = (i1, j1)
                        mn_ind = dist[(i1, j1)]
            if ind == now or mn_ind == 10 ** 9:
                break
            now = ind

    answer = []
    if dist[f] != 10 ** 9:
        cur = f
        while cur != s:
            answer.append(cur)
            cur = par[cur]
        answer.append(s)
        answer.reverse()
        return answer


if __name__ == "__main__":
    draw_anomalous(get_data_anomauls(), (5, 5), (38, 1))
