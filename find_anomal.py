import json


def get_data_anomauls():
    res = []
    json_response = json.load(open('data.json', mode='rb'))
    mp = {}
    for dat in json_response:
        for anom in dat['swans']:
            try:
                mp[anom['id']].append({'rate': anom['rate'], 'coords': dat['coords']})
            except KeyError:
                mp[anom['id']] = [{'rate': anom['rate'], 'coords': dat['coords']}]

    for id_anom in mp:
        best_x = 1
        best_y = 1
        sum_error = 100
        for x in range(1, 41):
            for y in range(1, 31):
                loc_sum_error = 0
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
        res.append((best_x, best_y, int0))
    return res
