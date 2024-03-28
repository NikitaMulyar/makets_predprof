import math

json_response = [{'coords': [9, 9], 'id': 1,
                  'swans': [{'id': '5b6eb38b', 'rate': 0.1626}, {'id': 'c00b92ba', 'rate': 0.249},
                            {'id': '931ede7b', 'rate': 1.4634}, {'id': '661c2e66', 'rate': 0.1859},
                            {'id': 'c2958c11', 'rate': 0.2006}, {'id': '08d55d4f', 'rate': 0.2602}]},
                 {'coords': [33, 9], 'id': 2,
                  'swans': [{'id': '5b6eb38b', 'rate': 0.2667}, {'id': 'c00b92ba', 'rate': 0.6186},
                            {'id': '931ede7b', 'rate': 0.1412}, {'id': '661c2e66', 'rate': 0.2262},
                            {'id': 'c2958c11', 'rate': 1.1475}, {'id': '08d55d4f', 'rate': 0.1918}]},
                 {'coords': [9, 23], 'id': 3,
                  'swans': [{'id': '5b6eb38b', 'rate': 0.262}, {'id': 'c00b92ba', 'rate': 0.1846},
                            {'id': '931ede7b', 'rate': 0.1592}, {'id': '661c2e66', 'rate': 0.2703},
                            {'id': 'c2958c11', 'rate': 0.1022}, {'id': '08d55d4f', 'rate': 0.6931}]},
                 {'coords': [32, 22], 'id': 4,
                  'swans': [{'id': '5b6eb38b', 'rate': 0.9231}, {'id': 'c00b92ba', 'rate': 0.4138},
                            {'id': '661c2e66', 'rate': 0.4587}, {'id': 'c2958c11', 'rate': 0.2006},
                            {'id': '08d55d4f', 'rate': 0.4142}]}]

mp = {}


for dat in json_response:
    for anom in dat['swans']:
        try:
            mp[anom['id']].append({'rate': anom['rate'], 'coords': dat['coords']})
        except KeyError:
            mp[anom['id']] = [{'rate': anom['rate'], 'coords': dat['coords']}]
print(mp)

for id_anom in mp:
    best_x = 1
    best_y = 1
    sum_error = 100
    for x in range(1, 41):
        for y in range(1, 31):
            loc_sum_error = 0
            #print(mp[id_anom])
            for i in range(0, len(mp[id_anom]) - 1):
                a = mp[id_anom][i]
                b = mp[id_anom][i + 1]
                ideal_k = a['rate'] / b['rate']
                pair_cor1 = a['coords']
                pair_cor2 = b['coords']
                sq_r1 = pow(pair_cor1[0] - x, 2) + pow(pair_cor1[1] - y, 2)
                sq_r2 = pow(pair_cor2[0] - x, 2) + pow(pair_cor2[1] - y, 2)
                if sq_r1 != 0:
                    real_k = sq_r2 / sq_r1
                    loc_sum_error += abs(real_k - ideal_k)
            if loc_sum_error < sum_error:
                sum_error = loc_sum_error
                best_x = x
                best_y = y
    sum_int0 = 0
    for ias in mp[id_anom]:
        pair_cor = ias['coords']
        sq_r = pow(pair_cor[0] - best_x, 2) + pow(pair_cor[1] - best_y, 2)
        sum_int0 += ias['rate'] * sq_r
    int0 = sum_int0 / len(mp[id_anom])
    print(best_x, best_y, int0)

# def data_circle(a, b):
#     k = math.sqrt(b['rate'] / a['rate'])
#     pair_cor1 = a['coords']
#     pair_cor2 = b['coords']
#     a = math.sqrt(pow(pair_cor1[0] - pair_cor1[1], 2) + pow(pair_cor2[0] - pair_cor2[1], 2))
#     r = k * a / (k * k - 1)
#     x0 = r
#     y0 = x0 * pair_cor1[1] / pair_cor1[0]
#     return r, x0, y0
#
# for id_anom in mp:
#     r1, x1, y1 = data_circle(mp[id_anom][0], mp[id_anom][1])
#     r2, x2, y2 = data_circle(mp[id_anom][1], mp[id_anom][2])
#     d = x1 * x1 + y1 * y1 - x2 * x2 - r1 * r1 + r2 * r2
#     A = 2 * (x2 - x1)
#     B = 2 * (y2 - y1)







