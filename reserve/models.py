from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

# Create your models here.abs

class TableReservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    requests = models.TextField(blank=True, null=True)
    number_of_guests = models.IntegerField(validators=[MaxValueValidator(8)])
    date_and_time = models.DateTimeField()

    def __str__(self):
        return self.name







