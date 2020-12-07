from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.

def index(request):
  context = {
    'sample_var': 'Hello, my name is Jeff',
    'bannerMotd': 'Unauthorized access is prohibited!',
    'hostname': 'R1-BLDG2'
  }

  return render(request, 'index.html', context)
