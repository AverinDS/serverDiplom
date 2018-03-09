import json

from django.http import HttpResponse, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import MobilePoints

NAME_DATA = 'points'

def index(request):
    return HttpResponse("INDEX PAGE")


# POST
@csrf_exempt
def perceptron(request):
    json_data = json.loads(request.POST.get(NAME_DATA))
    return JsonResponse(json_data, safe=False)