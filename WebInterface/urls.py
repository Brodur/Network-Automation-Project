from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('config/set-hostname', views.set_hostname, name="set_hostname"),
    path('config/set-banner', views.set_banner, name="set_banner")
]