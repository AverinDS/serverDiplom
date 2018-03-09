import json

from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

NAME_DATA = 'points'

def index(request):
    return HttpResponse("INDEX PAGE")


# POST
@csrf_exempt
def perceptron(request):
    json_data = json.loads(request.POST.get(NAME_DATA))
    return HttpResponse("PERCEPTRON RESULT")