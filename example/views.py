from django.shortcuts import render

# Create your views here.
from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import serializers
from models import Foo


class FooSerializer(serializers.ModelSerializer):
    class Meta:
        model = Foo
        fields = ('name',)


class FooViewset(ModelViewSet):
    queryset = Foo.objects.all()
    serializer_class = FooSerializer


router = DefaultRouter()
router.register('foo', FooViewset)
