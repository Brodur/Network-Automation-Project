from django.shortcuts import render, redirect
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

<<<<<<< HEAD
def index(request):
=======

def index(request):   
>>>>>>> d13215464a4c3a72e097c20ede8b0a9fcd529347
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
    'interfaces': allinterfaces['ietf-interfaces:interfaces']['interface']

  }

  return render(request, 'index.html', context)

def set_hostname(request):
    newHostname = hostname1.setHostname(request.POST.get('hostname-hostname'))
    return redirect('index')

def set_banner(request):
    newBanner = banner.setBanner(request.POST.get('banner-motd'))
    return redirect('index')

def set_password(request):
    newPassword = enablePassword.setEnablePassword(request.POST.get('enable-password'))
    return redirect('index')

def set_timeout(request):
    newMinutes = request.POST.get('console-timeout-minutes')
    newSeconds = request.POST.get('console-timeout-seconds')
    newTimeout = execTimeout.setExecTimeout(newMinutes, newSeconds)
    return redirect('index')

def set_interfaceAddress(request):
      interfaceNumber = request.POST.get('interfaces-interface')
      interfaceAddress = request.POST.get('interface-address')
      interfaceSubnet = request.POST.get('interface-subnet')
      newInterfaceAddress = intAddress.setInterfaceAddress(interfaceAddress, interfaceSubnet, interfaceNumber)
      return redirect('index')

def set_description(request):
      interfaceNumber = request.POST.get('interfaces-interface')
      interfaceDesc = request.POST.get('interface-description')
      newInterfaceDescription = intDescription.setInterfaceDescription(interfaceDesc, interfaceNumber)
      return redirect('index')
      
