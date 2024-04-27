from django.urls import path, include
from . import views

app_name = 'reserve'

urlpatterns = [
    path('', views.book_table ),]