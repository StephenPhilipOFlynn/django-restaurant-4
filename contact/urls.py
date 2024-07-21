from django.urls import path, include
from . import views

app_name = 'contact'

urlpatterns = [
    path('', views.contact_us , name='contact_us'),
    path('success/', views.contact_success, name='contact_success'),
    ]