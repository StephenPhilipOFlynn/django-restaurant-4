from django.shortcuts import render, redirect
from django.http import HttpResponse

# Create your views here.
from .models import TableReservation
from .forms import ReserveForm

def reservation_success(request):
    return render(request, 'Reserve/success.html')

def book_table(request):
    reserve_form = ReserveForm()

    if request.method == 'POST':
        reserve_form = ReserveForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
            return redirect('reserve:reservation_success')
            
    context = {'form': reserve_form}
    
    return render(request, 'Reserve/reserve.html' , context)
