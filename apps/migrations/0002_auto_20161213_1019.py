# -*- coding: utf-8 -*-
# Generated by Django 1.10.4 on 2016-12-13 10:19
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResourceAction',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('method', models.CharField(max_length=7)),
                ('url', models.CharField(max_length=255)),
            ],
        ),
        migrations.RemoveField(
            model_name='resource',
            name='allowed_methods',
        ),
        migrations.AddField(
            model_name='resourceaction',
            name='resource',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='actions', to='apps.Resource'),
        ),
    ]