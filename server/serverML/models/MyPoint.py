from django.db import models
from rest_framework import serializers


class MyPoint(models.Model):
    first = models.IntegerField(default=0) #x
    second = models.IntegerField(default=0)#y

    class Meta:
        db_table = "point"

    def __str__(self):
        return "x:" + str(self.x) + "y:"+str(self.y)


class PointSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyPoint
        fields = ('first', 'second',)
