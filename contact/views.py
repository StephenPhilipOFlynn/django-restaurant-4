from django.shortcuts import render, redirect
from .forms import ContactForm

# Create your views here.
from .models import Contact

def contact_us(request):
    contact_form = ContactForm()

    if request.method == 'POST':
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            contact_form.save()

    context = {'form': contact_form}
    
    return render(request, 'Contact/contact.html' , context)