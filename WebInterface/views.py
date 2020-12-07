from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import json
from .Classes.Hostname import *

# Create your views here.

def index(request):
  context = {

    'sample_var': 'Hostname.getHostname'
    'sample_var': 'Hello, my name is Jeff',
    'bannerMotd': 'Unauthorized access is prohibited!',
    'hostname': 'R1-BLDG2'
  }

  return render(request, 'index.html', context)
  print(Hostname.getHostname())