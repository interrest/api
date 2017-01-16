from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import serializers
from models import Resource
from action_resource import ResourceActionSerializer


class ResourceSerializer(serializers.ModelSerializer):
    actions = ResourceActionSerializer(many=True, read_only=True)

    class Meta:
        model = Resource
        fields = '__all__'


class ResourceViewset(ModelViewSet):
    queryset = Resource.objects.all()
    serializer_class = ResourceSerializer
    filter_fields = ('app',)


router = DefaultRouter()
router.register('resource', ResourceViewset)
