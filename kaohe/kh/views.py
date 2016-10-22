# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from kh.models import Date, Weather, Temperature
from django.shortcuts import render


# Create your views here.
def home(request):
    date = Date.objects.all()[:4]
    weather = Weather.objects.all()[:4]
    temp = Temperature.objects.all()[:4]
    context={'date':list(date),'weather':list(weather),'temp': list(temp)}
    return render(request, 'home.html', context)
