from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import Meal

def menu_list(request):
    menu_list = Meal.objects.all()
    context = {'menu_list': menu_list}
    return render(request , 'menu/templates/list.html', context)
