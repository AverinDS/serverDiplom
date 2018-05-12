import numpy as np


def prepare_x_predict(max_x):
    first_x_for_predict = max_x
    step = 5
    count_points_of_predict = 30

    x_predict = [i for i in range(first_x_for_predict + step,
                                  first_x_for_predict + (step * count_points_of_predict),
                                  step)]

    return np.array(x_predict).reshape(-1, 1)
