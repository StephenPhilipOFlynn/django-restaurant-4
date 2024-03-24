from django.shortcuts import render
from .models import OurRestaurant , ChefsInfo

# Create your views here.
def ourrestaurant_list(request):
    about = OurRestaurant.objects.all()
    chefs = ChefsInfo.objects.all()
    
    context = {
        'about' : about,
        'chefs' : chefs
    }
    return render(request , 'ourrestaurant/about.html' , context)


