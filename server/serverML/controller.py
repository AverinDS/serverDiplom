import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .ML.perceptron import MyPerceptron
from .models.MyPoint import MyPoint
import numpy as np
from .models.MyPoint import PointSerializer as Serializer

NAME_DATA = "points"


def index(request):
    return HttpResponse("INDEX PAGE")


# POST
@csrf_exempt
def perceptron(request):

    json_data = json.loads(request.POST.get(NAME_DATA))  # getting form data
    json_data = json_data[NAME_DATA]

    perceptron_model = MyPerceptron()
    x, y = perceptron_model.make_data_from_json(json_data)
    perceptron_model.fitting_perceptron(x, y)

    x_test = np.array([211, 220, 230, 240, 250]).reshape(-1, 1)
    y_predict = perceptron_model.get_predict_perceptron(x_test)

    x_test = x_test.ravel()
    y_predict = y_predict.ravel()

    list_of_points = []
    for i in range(len(x_test)):
        point = MyPoint()
        point.x = x_test[i]
        point.y = y_predict[i]
        list_of_points.append(point)

    return JsonResponse(Serializer(list_of_points, many=True).data, safe=False)

