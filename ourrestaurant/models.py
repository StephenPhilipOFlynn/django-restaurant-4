from django.db import models

# Create your models here.
class OurRestaurant(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to="ourrestaurant/")

    def __str__(self):
        return self.title

class ChefsInfo(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="ourrestaurant/")

    def __str__(self):
        return self.name

