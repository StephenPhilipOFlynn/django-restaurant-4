from django.db import models

# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length = 50)
    description = models.Textfield()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField(upload_to="menu/")