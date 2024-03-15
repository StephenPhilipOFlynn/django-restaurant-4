from django.db import models


# Create your models here.
class Meal(models.Model):
    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField(upload_to="menu/")
    
    def __str__(self):
        return self.name