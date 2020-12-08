from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import json
from .Classes.Hostname import *
from .Classes.Banner import *
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
hostname1 = Hostname('10.10.20.48','developer','C1sco12345')
banner = Banner('10.10.20.48','developer','C1sco12345')

def index(request):   
  hostname = hostname1.getHostname()
  hostname = hostname['Cisco-IOS-XE-native:hostname']   
  returnedBanner = banner.getBanner()
  returnedBanner =returnedBanner['Cisco-IOS-XE-native:banner']  


  context = {
    'bannerMotd': returnedBanner,
    'hostname': hostname
  }

  return render(request, 'index.html', context)


@csrf_exempt
def set_hostname(request):
#     host
    newHostname = hostname1.setHostname(request.POST.get('hostname-hostname'))
    return HttpResponse(newHostname)
@csrf_exempt
def set_banner(request):
    return HttpResponse('banner banner banner')
