from django.conf.urls import url

from . import controller


urlpatterns = [
    url(r'^$', controller.index, name='index'),
    url(r'^perceptron$', controller.perceptron, name='perceptron'),
]