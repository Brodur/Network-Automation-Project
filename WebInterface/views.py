from django.shortcuts import render
from django.http import HttpResponse
import requests
import sys
import json
from Hostname import *

# Create your views here.

# def index(request):
#   context = {
#     'sample_var': 'Hostname.getHostname',
#     'sample_var': 'Hello, my name is Jeff',
#     'bannerMotd': 'Unauthorized access is prohibited!',
#     'hostname': 'R1-BLDG2'
#   }

#   return render(request, 'index.html', context)
hostname1 = Hostname('10.10.20.48','developer','C1sco12345','CSRV-1')
abcd = hostname1.getHostname()


# returnedHostname = hostname1.getHostname()
# hostname1 = hostname1.setHostname()
# print(returnedHostname)
