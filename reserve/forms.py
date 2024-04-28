from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import TableReservation

class ReserveForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = ['name', 'email', 'phone', 'requests', 'number_of_guests', 'date_and_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'reserve-form-name'}),
            'email': forms.EmailInput(attrs={'class': 'reserve-form-email'}),
            'phone': forms.TextInput(attrs={'class': 'reserve-form-phone'}),
            'requests': forms.Textarea(attrs={'class': 'reserve-form-requests'}),
            'number_of_guests': forms.NumberInput(attrs={'class': 'reserve-form-email'}),
            'date_and_time': forms.DateTimeInput(attrs={'class': 'reserve-form-date-and-time', 'type': 'datetime-local', 'step': '1800'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'requests': 'Special Requests',
            'number_of_guests': 'Number of Guests',
            'date_and_time': 'Date and Time',
        }