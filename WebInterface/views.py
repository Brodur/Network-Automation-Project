from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import json
from Hostname import *
from GetBanner import *

# Create your views here.

def index(request):
  context = {
<<<<<<< HEAD
    'sample_var': 'Hostname.getHostname'
  }

  return render(request, 'index.html', context)

=======
    'sample_var': 'Hello, my name is Jeff',
    'bannerMotd': 'Unauthorized access is prohibited!',
    'hostname': 'R1-BLDG2'
  }

  return render(request, 'index.html', context)
>>>>>>> origin/master
