from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator
from .models import TableReservation

class ReserveForm(forms.ModelForm):
    # Enforce number of guests to be between 1 and 8 on client side of form
    number_of_guests = forms.IntegerField(
        validators=[MinValueValidator(1), MaxValueValidator(8)],
        widget=forms.NumberInput(attrs={'class': 'reserve-form-guests', 'min': 1, 'max': 8})
    )

    class Meta:
        model = TableReservation
        fields = ['name', 'email', 'phone', 'requests', 'number_of_guests', 'date_and_time']
        widgets = {
            'name': forms.TextInput(attrs={'class': 'reserve-form-name'}),
            'email': forms.EmailInput(attrs={'class': 'reserve-form-email'}),
            'phone': forms.TextInput(attrs={'class': 'reserve-form-phone'}),
            'requests': forms.Textarea(attrs={'class': 'reserve-form-requests'}),
            'date_and_time': forms.DateTimeInput(attrs={'class': 'reserve-form-date-and-time', 'type': 'datetime-local', 'step': '1800', 'id': 'reserve_date_and_time'}),
        }
        labels = {
            'name': 'Name',
            'email': 'Email',
            'phone': 'Phone Number',
            'requests': 'Special Requests',
            'number_of_guests': 'Number of Guests',
            'date_and_time': 'Date and Time',
        }