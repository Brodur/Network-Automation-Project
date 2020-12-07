from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import json
from .Classes.Hostname import *

# Create your views here.

def index(request):
  hostname1 = Hostname('10.10.20.48','developer','C1sco12345')
  hostname = hostname1.getHostname()
#   hostname = json.loads(hostname)
  hostname = hostname['Cisco-IOS-XE-native:hostname']
  context = {
    'sample_var': hostname,
    'bannerMotd': 'afsdfsdfsaseawe1 ibited!',
    'hostname': hostname
  }

  return render(request, 'index.html', context)
#   print(Hostname.getHostname())
