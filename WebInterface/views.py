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
from .Classes.Interfaces import *
from django.views.decorators.csrf import csrf_exempt



# Create your views here.
hostname1 = Hostname('10.10.20.48','developer','C1sco12345')
banner = Banner('10.10.20.48','developer','C1sco12345')
enablePassword = EnablePassword('10.10.20.48','developer','C1sco12345')
execTimeout = ExecTimeout('10.10.20.48','developer','C1sco12345')
intAddress = InterfaceAddress('10.10.20.48','developer','C1sco12345')
intDescription = InterfaceDescription('10.10.20.48','developer','C1sco12345')
interfaces = Interfaces('10.10.20.48','developer','C1sco12345')



def index(request):   
  # get the hostname from the json for the router
  hostname = hostname1.getHostname()
  hostname = hostname['Cisco-IOS-XE-native:hostname']   

  # get the banner from the json for router
  returnedBanner = banner.getBanner()
  returnedBanner = returnedBanner['Cisco-IOS-XE-native:banner'] 

  # get the PASSWORD for the console line
  password = enablePassword.getEnablePassword()
  if password:
        password = password['Cisco-IOS-XE-native:secret']
  else:
        password = password
  

  # console timeout separated in minutes and seconds
  timeout = execTimeout.getExecTimeout()
  minuteTimeout = timeout['Cisco-IOS-XE-native:console'][0]['exec-timeout']['minutes']
  secondsTimeout = timeout['Cisco-IOS-XE-native:console'][0]['exec-timeout']['seconds']

  # ip address for the passed interface with separate ip address and subnet mask
  ipAddress = intAddress.getInterfaceAddress('GigabitEthernet1')
  interfaceIpAddress = ipAddress['ietf-ip:address'][0]['ip']
  interfaceSubnetMask = ipAddress['ietf-ip:address'][0]['netmask']
  
  # interface description for the selected interface
  interfaceDesc = intDescription.getInterfaceDescription('GigabitEthernet1')
  interfaceDesc = interfaceDesc['ietf-interfaces:description']

  # get all the interfaces in the context but is in json
  allinterfaces = interfaces.getInterfaceAddress()




  context = {
    'bannerMotd': returnedBanner,
    'hostname': hostname,
    'enablePassword': password,
    'consoleTimeoutminutes': minuteTimeout,
    'consoleTimeoutSeconds': secondsTimeout,
    'interfaceIpAddress': interfaceIpAddress,
    'interfaceSubnetMask': interfaceSubnetMask,
    'interfaceDesc': interfaceDesc,
    'interfaces': allinterfaces
  }

  return render(request, 'index.html', context)



def set_hostname(request):      
    newHostname = hostname1.setHostname(request.POST.get('hostname-hostname'))
    return HttpResponse(newHostname)


def set_banner(request):
    newBanner = banner.setBanner(request.POST.get('banner-motd'))
    return HttpResponse(newBanner)


def set_password(request):
    newPassword = enablePassword.setEnablePassword(request.POST.get('enabe-password'))
    return HttpResponse(newPassword)
