# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Date, Weather, Temperature
# Register your models here.
admin.site.register(Date)
admin.site.register(Weather)
admin.site.register(Temperature)