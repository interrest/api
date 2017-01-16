from rest_framework.viewsets import ModelViewSet
from rest_framework.routers import DefaultRouter
from rest_framework import serializers
from rest_framework.permissions import IsAuthenticated
from models import App


class AppSerializer(serializers.ModelSerializer):
    class Meta:
        model = App
        fields = '__all__'


class AppViewset(ModelViewSet):
    queryset = App.objects.all()
    serializer_class = AppSerializer
    permission_classes = (IsAuthenticated,)


router = DefaultRouter()
router.register('app', AppViewset)