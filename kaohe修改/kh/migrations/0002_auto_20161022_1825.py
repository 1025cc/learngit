# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2016-10-22 10:25
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kh', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='date',
            name='date',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='temperature',
            name='temp',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='weather',
            name='day',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='weather',
            name='night',
            field=models.CharField(max_length=200),
        ),
    ]
