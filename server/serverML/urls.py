from django.conf.urls import url

from . import controller


urlpatterns = [
    url(r'^$', controller.index, name='index'),
    url(r'^perceptron$', controller.perceptron, name='perceptron'),
    url(r'^linear$', controller.linear_regression, name='linear'),
    url(r'^mlpclassifier$', controller.mlp_classifier, name='mlpclassifier'),
    url(r'^mlpregressor$', controller.mlp_regressor, name='mlpregressor'),
    url(r'^mynetwork$', controller.neyron_network, name='mynetwork'),
    url(r'^fblib$', controller.fb_lib, name='fblib'),
]