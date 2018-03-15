# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render, redirect
import os
import geoip2.database
import traceback

db_file_path = os.path.join(os.path.dirname(os.path.abspath(__name__)), 'static/files/GeoLite2-Country.mmdb')
reader = geoip2.database.Reader(db_file_path)

ASIA_COUNTRY_CODE = ["JP", "CN", "HK", "KP"]
DOCKER_IMAGE_HOSTS = {
    "tokyo": "https://tier4data.blob.core.windows.net/images/dpx2_autoware.1.6.2.tar",
    "us": "https://tier4dataus.blob.core.windows.net/images/dpx2_autoware.1.6.2.tar",
}

def get_client_ip(request):
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    return ip

def index(request):
    return render(request, 'welcome_page/index.html')

#def development(request):
#    return render(request, 'welcome_page/development.html')

def join(request):
    return render(request, 'welcome_page/join.html')

def development(request):
    return render(request, 'welcome_page/development.html')

def development2(request):
    return render(request, 'welcome_page/development2.html')

def docker_x86_install(request):
    return redirect('https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-Generic-x86')
    # return render(request, 'welcome_page/docker_x86.html')

def docker_px2_install(request):
    # return render(request, 'welcome_page/docker_px2_tier4.html')
    return redirect('https://github.com/CPFL/Autoware/wiki/Installation-by-Docker:-DRIVE-PX2')

def sample_data1(request):
    return redirect('https://autoware.blob.core.windows.net/sample/sample_moriyama_data.tar.gz')

def sample_data2(request):
    return redirect('https://autoware.blob.core.windows.net/sample/my_launch.sh')

def sample_data3(request):
    return redirect('https://autoware.blob.core.windows.net/sample/sample_moriyama_150324.tar.gz')

def docker_image_px2(request):
    try:
        country_code = None
        try:
            request_ip = get_client_ip(request)
            record = reader.country(request_ip)
            country_code = record.country.iso_code
        except:
            country_code = "US"
        print request_ip, country_code
        if country_code in ASIA_COUNTRY_CODE:
            return redirect(DOCKER_IMAGE_HOSTS["tokyo"])
        else:
            return redirect(DOCKER_IMAGE_HOSTS["us"])
    except:
        print traceback.format_exc()
        return render(request, 'welcome_page/join.html')
