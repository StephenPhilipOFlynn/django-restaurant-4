"""
URL configuration for my_project project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from restaurant import views as index_views
from menu import views as menu_views
from gallery import views as gallery_views

urlpatterns = [
    path('', index_views.index, name='home'),
    path('menu/', menu_views.index, name='menu'),
    path('gallery/', gallery_views.index, name='gallery'),
    path('admin/', admin.site.urls),
]
