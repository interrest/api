from __future__ import unicode_literals

from django.db import models
from django.conf import settings

# Create your models here.
class App(models.Model):
    name = models.CharField(max_length=255)
    base_url = models.CharField(max_length=255)
    user = models.ForeignKey(settings.AUTH_USER_MODEL,
                             on_delete=models.CASCADE,
                             related_name='apps')


class Resource(models.Model):
    name = models.CharField(max_length=255)
    base_url = models.CharField(max_length=255)
    app = models.ForeignKey(App,
                            on_delete=models.CASCADE,
                            related_name='resources')


class ResourceAction(models.Model):
    name = models.CharField(max_length=255)
    method = models.CharField(max_length=7)
    url = models.CharField(max_length=255)
    resource = models.ForeignKey(Resource,
                                 on_delete=models.CASCADE,
                                 related_name='actions')
