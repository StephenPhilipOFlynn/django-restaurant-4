from django import forms
from .models import Contact

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['name', 'subject', 'email', 'message']
        widgets = {
            'name': forms.TextInput(attrs={'class':'contact-form-name'}),
            'subject': forms.TextInput(attrs={'class': 'contact-form-subject'}),
            'email': forms.EmailInput(attrs={'class': 'contact-form-email'}),
            'message': forms.TextInput(attrs={'class': 'contact-form-message'}),
        }
        labels = {
            'name': 'Your Name',
            'subject': 'Subject',
            'email': 'Email Address',
            'message': 'Message',
        }