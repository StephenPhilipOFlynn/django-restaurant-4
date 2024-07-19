from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Meal

def menu_view(request):
    starters = Meal.objects.filter(category=Meal.STARTER)
    main_courses = Meal.objects.filter(category=Meal.MAIN_COURSE)
    desserts = Meal.objects.filter(category=Meal.DESSERT)
    drinks = Meal.objects.filter(category=Meal.DRINK)
   
    context = {
        'starters': starters,
        'main_courses': main_courses,
        'desserts': desserts,
        'drinks': drinks,
    }
    return render(request, 'menu.html', context)
