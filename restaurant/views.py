from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def restaurant(request):
    context = {}

    return render(request, 'restaurant/index.html', context)
