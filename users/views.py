from rest_framework import serializers
from rest_framework import viewsets
from django.contrib.auth.models import User
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.routers import DefaultRouter


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ('password',)


class UserViewset(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = (IsAuthenticated,)

    def retrieve(self, request, pk=None, **kwargs):
        if pk == 'me':
            user = self.get_queryset().get(id=request.user.pk)
            serialized = self.get_serializer(user)
            return Response(serialized.data)
        else:
            super(UserViewset, self).retrieve(request, pk=pk, **kwargs)


router = DefaultRouter()
router.register('user', UserViewset)