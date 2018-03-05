from django.conf.urls import url

from . import controller


urlpatterns = [
    url(r'^$', controller.index, name='index'),
    url(r'^$', controller.perceptron, name='perceptron'),
]