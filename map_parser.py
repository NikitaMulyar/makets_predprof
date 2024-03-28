from PIL import Image, ImageDraw
from math import sqrt


width = 40
height = 30

matrix = {(i, j): [] for i in range(width) for j in range(height)}
used_cells = set()


def fill_graph():
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


def draw_anomalous(arr):
    """
    :param arr: List of tuples like: (x, y, val), where
    val - maximum value of the anomalous in (x, y)
    :return:
    """
    im = Image.open("map.png")
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
            outline=(250, 0, 0), width=5)
        for i in range(width):
            for j in range(height):
                if x1 <= i * 50 <= x2 and y1 <= j * 50 <= y2:
                    used_cells.add((i, j))

    fill_graph()
    import pprint
    pprint.pp(matrix)
    im.save("map2.png")



#print(matrix)
draw_anomalous([(10, 10, 29), (15, 15, 30), (30, 30, 3)])


s = (0, 0)
f = (35, 25)
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
    print(answer)
