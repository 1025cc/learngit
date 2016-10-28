# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models



# Create your models here.


class Date(models.Model):
    date = models.CharField(max_length=20)

    def __unicode__(self):
        return self.date


class Weather(models.Model):
    day = models.CharField(max_length=20)
    night = models.CharField(max_length=20)

    def __unicode__(self):
        return self.day


class Temperature(models.Model):
    temp = models.CharField(max_length=20)

    def __unicode__(self):
        return self.temp
