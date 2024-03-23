from django.contrib import admin

# Register your models here.
from .models import OurRestaurant , ChefsInfo

# Admin
admin.site.register(OurRestaurant)
admin.site.register(ChefsInfo)