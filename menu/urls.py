from django.urls import path, include
from . import views

app_name = 'menu'

urlpatterns = [
    path('', views.menu_list, name='menu'),]