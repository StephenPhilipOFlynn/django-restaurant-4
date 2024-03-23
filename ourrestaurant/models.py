from django.db import models

# Create your models here.
class OurRestaurant(models.Model):
    title = models.CharField(max_length = 50)
    content = models.TextField()
    image = models.ImageField(upload_to="ourrestaurant/")

    class Meta:
        verbose_name_plural = "Our Restaurant"

    def __str__(self):
        return self.title

class ChefsInfo(models.Model):
    name = models.CharField(max_length=100)
    bio = models.TextField()
    image = models.ImageField(upload_to="ourrestaurant/")

    class Meta:
        verbose_name_plural = "Chef's Bio"

    def __str__(self):
        return self.name

