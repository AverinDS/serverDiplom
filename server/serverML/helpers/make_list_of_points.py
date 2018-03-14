from ..models.MyPoint import MyPoint


def make_list_of_points(x_predict, y_predict):
    x_predict = x_predict.ravel()
    y_predict = y_predict.ravel()

    # print(y_predict)

    list_of_points = []
    for i in range(len(x_predict)):
        point = MyPoint()
        point.x = x_predict[i]
        point.y = y_predict[i]
        list_of_points.append(point)

    return list_of_points
