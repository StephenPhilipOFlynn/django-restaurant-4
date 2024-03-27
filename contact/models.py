from django.db import models

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100, help_text="Enter your name")
    subject = models.CharField(max_length=100, help_text="Enter your subject")
    email = models.EmailField(help_text="Enter your email address")
    message = models.CharField(max_length=500, help_text="Enter your message")

    def __str__(self):
        return self.name
    