from django.http import HttpResponse


def index(request):
    return HttpResponse("INDEX PAGE")

def perceptron(request):
    return HttpResponse("PERCEPTRON RESULT")