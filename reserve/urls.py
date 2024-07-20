from django.urls import path, include
from . import views

app_name = 'reserve'

urlpatterns = [
    path('', views.book_table, name='book_table'),
    path('success/', views.reservation_success, name='reservation_success'),
]