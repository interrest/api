from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import serializers
from models import ResourceAction


class ResourceActionSerializer(serializers.ModelSerializer):
    class Meta:
        model = ResourceAction
        fields = '__all__'


class ResourceActionViewset(ModelViewSet):
    queryset = ResourceAction.objects.all()
    serializer_class = ResourceActionSerializer
    filter_fields = ('resource',)


router = DefaultRouter()
router.register('resource-action', ResourceActionViewset)
