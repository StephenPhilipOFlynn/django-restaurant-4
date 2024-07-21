from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator
from django.core.exceptions import ValidationError
from django.utils import timezone
import datetime

# Create your models here

class TableReservation(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    phone = models.CharField(max_length=15)
    requests = models.TextField(blank=True, null=True, max_length=200)
    number_of_guests = models.IntegerField(validators=[MaxValueValidator(8)])
    date_and_time = models.DateTimeField()

    def clean(self):
        if self.date_and_time:
            # no bookings in the past
            if self.date_and_time < timezone.now():
                raise ValidationError('The booking must be in the future')
        
            # no bookings more than two months from now
            two_months_later = timezone.now() + datetime.timedelta(days=60)
            if self.date_and_time > two_months_later:
                raise ValidationError('Bookings cannot be made more than two months ahead')
        
            #booking between 12 noon and 10pm
            booking_time = self.date_and_time.time()
            if not (booking_time >= datetime.time(12, 0) and booking_time <= datetime.time(22, 0)):
                raise ValidationError('Bookings must be between 12noon and 10pm')

        else:
            raise ValidationError('Date and time is required')

    def __str__(self):
        return self.name