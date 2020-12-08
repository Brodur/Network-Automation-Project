from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import json
from .Classes.Hostname import *
from .Classes.Banner import *
from .Classes.EnablePassword import *
from .Classes.ExecTimeout import *
from .Classes.InterfaceAddress import *
from .Classes.InterfaceDescription import *
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
hostname1 = Hostname('10.10.20.48','developer','C1sco12345')
banner = Banner('10.10.20.48','developer','C1sco12345')
# enPassword = EnablePassword('10.10.20.48','developer','C1sco12345')
# execTimout = ExecTimeout('10.10.20.48','developer','C1sco12345')
# intAddress = InterfaceAddress('10.10.20.48','developer','C1sco12345')
# intDescription = InterfaceDescription('10.10.20.48','developer','C1sco12345')



def index(request):   
  hostname = hostname1.getHostname()
  hostname = hostname['Cisco-IOS-XE-native:hostname']   
  returnedBanner = banner.getBanner()
  returnedBanner = returnedBanner['Cisco-IOS-XE-native:banner'] 
  # password = enPassword.getEnablePassword() 
  # password = password['Cisco-IOS-XE-native:']
  # timeout = execTimeout.getExecTimeout()
  # timeout = timeout['Cisco-IOS-XE-native:']
  # ipAddress = intAddress.getInterfaceAddress()
  # ipAddress = ipAddress['Cisco-IOS-XE-native:']
  # interfaceDesc = intDescription.getInterfaceDescription()
  # interfaceDesc = interfaceDesc['Cisco-IOS-XE-native:']



  context = {
    'bannerMotd': returnedBanner,
    'hostname': hostname
  }

  return render(request, 'index.html', context)


@csrf_exempt
def set_hostname(request):      
    newHostname = hostname1.setHostname(request.POST.get('hostname-hostname'))
    return HttpResponse(newHostname)

@csrf_exempt
def set_banner(request):
    newBanner = banner.setBanner(request.POST.get('banner-motd'))
    return HttpResponse(newBanner)
