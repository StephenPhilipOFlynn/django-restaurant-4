from django import forms
from .models import TableReservation

class ReserveForm(forms.ModelForm):
    class Meta:
        model = TableReservation
        fields = '__all__'