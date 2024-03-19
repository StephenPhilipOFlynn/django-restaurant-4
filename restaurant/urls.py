from django.urls import path, include
from . import views

app_name = 'restaurant'

# correct the below url path
urlpatterns = [
    path('', views.restaurant , name="restaurant" ),]