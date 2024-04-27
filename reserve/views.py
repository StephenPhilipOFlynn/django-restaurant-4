from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from .models import TableReservation
from .forms import ReserveForm

def book_table(request):
    """
    reserve_form = ReserveForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if reserve_form.is_valid():
            reserve_form.save()
    """
    context = {'form': ReserveForm}
    
    return render(request, 'Reserve/reserve.html' , context)