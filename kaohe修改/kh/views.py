# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kh.models import Date, Weather, Temperature
from django.shortcuts import render


# Create your views here.
def home(request):
    dates = Date.objects.all().reverse()[:4]
    weathers = Weather.objects.all().reverse()[:4]
    temps = Temperature.objects.all().reverse()[:4]
    context={'dates':list(dates),'weathers':list(weathers),'temps': list(temps)}
    return render(request, 'home.html', context)
