# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations
from django.conf import settings


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inmueble',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('titulo', models.CharField(max_length=60)),
                ('descripcion', models.CharField(max_length=20, null=True, blank=True)),
                ('banos', models.CharField(max_length=5, null=True, blank=True)),
                ('habitaciones', models.CharField(max_length=5, null=True, blank=True)),
                ('metros_terreno', models.CharField(max_length=5, null=True, blank=True)),
                ('metros_cubiertos', models.CharField(max_length=5, null=True, blank=True)),
                ('email', models.EmailField(max_length=75, null=True)),
                ('info', models.TextField(null=True, blank=True)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('fecha_publicacion', models.DateTimeField(null=True, blank=True)),
                ('creador', models.ForeignKey(to=settings.AUTH_USER_MODEL)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
