from django.db import models
from rest_framework import serializers


class MobilePoints(models.Model):
    points = [[models.FloatField, models.FloatField]]


class MobilePointsSerializer(serializers.ModelSerializer):
    class Meta:
        model = MobilePoints
        fields = ('points')