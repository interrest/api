"""interrest URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import include, url
from django.contrib import admin
from rest_framework.authtoken.views import obtain_auth_token
from apps import app_resource, resource_resource, action_resource
from example.views import router
from users import views

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^', include(app_resource.router.get_urls())),
    url(r'^', include(resource_resource.router.get_urls())),
    url(r'^', include(action_resource.router.get_urls())),
    url(r'^', include(views.router.get_urls())),
    url(r'^example/', include(router.get_urls())),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    url(r'^auth/', obtain_auth_token)
]
