from django.db import models
from django.utils import timezone

# Create your models here.
class Contact(models.Model):
    name = models.CharField(max_length=100)
    subject = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.CharField(max_length=500)
    received_at = models.DateTimeField(auto_now_add=True, help_text="Message received at")

    class Meta:
        verbose_name_plural = "Contact"

    def __str__(self):
        return self.name
    