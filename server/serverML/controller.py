from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt

from .ML.perceptron import MyPerceptron
from .ML.mlp_classifier import MyMlpClassifier
from .ML.linear_regressor import MyLinearRegression
from .ML.mlp_regressor import MyMLPRegressor

from .models.MyPoint import PointSerializer as Serializer
from .helpers.make_data_from_json import make_data_from_json
from .helpers.prepare_x_predict import prepare_x_predict
from .helpers.make_list_of_points import make_list_of_points
from .helpers.get_gson_data import get_gson_data


def index(request):
    return HttpResponse("INDEX PAGE")


# POST
@csrf_exempt
def perceptron(request):
    json_data = get_gson_data(request)
    x, y = make_data_from_json(json_data)

    perceptron_model = MyPerceptron()
    perceptron_model.fitting(x, y)

    x_predict = prepare_x_predict(int(max(x)))
    y_predict = perceptron_model.get_predict(x_predict)

    list_of_points = make_list_of_points(x_predict, y_predict)

    return JsonResponse(Serializer(list_of_points, many=True).data, safe=False)


# POST
@csrf_exempt
def mlp_classifier(request):
    json_data = get_gson_data(request)
    x, y = make_data_from_json(json_data)

    my_classifier = MyMlpClassifier()
    my_classifier.fitting(x, y)

    x_predict = prepare_x_predict(int(max(x)))
    y_predict = my_classifier.get_predict(x_predict)

    list_of_points = make_list_of_points(x_predict, y_predict)

    return JsonResponse(Serializer(list_of_points, many=True).data, safe=False)


# POST
@csrf_exempt
def linear_regression(request):
    json_data = get_gson_data(request)
    x, y = make_data_from_json(json_data)

    my_linear_regr = MyLinearRegression()
    my_linear_regr.fitting(x, y)

    x_predict = prepare_x_predict(int(max(x)))
    y_predict = my_linear_regr.get_predict(x_predict)

    list_of_points = make_list_of_points(x_predict, y_predict)

    return JsonResponse(Serializer(list_of_points, many=True).data, safe=False)


# POST
@csrf_exempt
def mlp_regressor(request):
    json_data = get_gson_data(request)
    x, y = make_data_from_json(json_data)

    mlp_regr = MyMLPRegressor()
    mlp_regr.fitting(x, y)

    x_predict = prepare_x_predict(int(max(x)))
    y_predict = mlp_regr.get_predict(x_predict)

    list_of_points = make_list_of_points(x_predict, y_predict)

    return JsonResponse(Serializer(list_of_points, many=True).data, safe=False)
