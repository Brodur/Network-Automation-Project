from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('config/set-hostname', views.set_hostname, name="set_hostname"),
    path('config/set-banner', views.set_banner, name="set_banner"),
    path('config/set-enable-password', views.set_password, name="set_password"),
    # path('config/set-console-timeout', views.set_timeout, name="set_timeout"),
    # path('config/set-interface-ip', views.set_address, name="set_address"),
    # path('config/set-interface-description', views.set_description, name="set_description")
]
