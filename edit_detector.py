import json


def edit_detector(id_point, coors, anomalia_1, anomalia_2, anomalia_3, anomalia_4, anomalia_5, anomalia_6):
    if not 0 <= coors[0] <= 40 or not 0 <= coors[1] <= 30:
        return -1, 'Bad coordinates'
    file = json.load(open('data.json', 'rb'))
    fl = False
    try:
        for el in file:
            if el['id'] == id_point:
                fl = True
                for i in el['swans']:
                    if i['id'] == anomalia_1[0] and anomalia_1[1] is not None:
                        i['rate'] = anomalia_1[1]
                    elif i['id'] == anomalia_2[0] and anomalia_2[1] is not None:
                        i['rate'] = anomalia_2[1]
                    elif i['id'] == anomalia_3[0] and anomalia_3[1] is not None:
                        i['rate'] = anomalia_3[1]
                    elif i['id'] == anomalia_4[0] and anomalia_4[1] is not None:
                        i['rate'] = anomalia_4[1]
                    elif i['id'] == anomalia_5[0] and anomalia_5[1] is not None:
                        i['rate'] = anomalia_5[1]
                    elif i['id'] == anomalia_6[0] and anomalia_6[1] is not None:
                        i['rate'] = anomalia_6[1]
                break
    except Exception:
        return -1, 'Bad request'
    if not fl:
        return -1, 'No such point'
    json.dump(file, open('data.json', 'w'))
    return 0, 'Successfully edited detector'
