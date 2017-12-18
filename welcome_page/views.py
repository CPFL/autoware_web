# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'welcome_page/index.html')

def docker_x86_install(request):
    return render(request, 'welcome_page/docker_x86.html')

def docker_px2_install(request):
    return render(request, 'welcome_page/docker_px2.html')
