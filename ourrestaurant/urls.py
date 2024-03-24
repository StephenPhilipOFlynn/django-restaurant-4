from django.urls import path, include
from . import views

app_name = 'ourrestaurant'

urlpatterns = [
    path('', views.ourrestaurant_list , name='ourrestaurant_list' ),]