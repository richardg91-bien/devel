# -*- coding: utf-8 -*-
# Generated by Django 1.10.2 on 2016-10-16 21:02
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('inmo', '0004_auto_20161016_1737'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='barrio',
            options={'verbose_name_plural': 'Barrios'},
        ),
        migrations.AlterModelOptions(
            name='ciudad',
            options={'verbose_name_plural': 'Ciudades'},
        ),
        migrations.AlterModelOptions(
            name='cliente',
            options={'verbose_name_plural': 'Clientes'},
        ),
        migrations.AlterModelOptions(
            name='inmueble',
            options={'verbose_name_plural': 'Inmuebles'},
        ),
        migrations.AlterModelOptions(
            name='mensaje',
            options={'verbose_name_plural': 'Mensajes'},
        ),
        migrations.AlterModelOptions(
            name='pais',
            options={'verbose_name_plural': 'Paises'},
        ),
    ]