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