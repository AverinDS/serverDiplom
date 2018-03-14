import numpy as np


def make_data_from_json(request):
    x = []
    y = []

    for i in request:
        x.append(i['first'])
        y.append(i['second'])

    x = np.array(x).reshape(-1, 1)
    y = np.array(y).reshape(-1, 1)
    return x, y