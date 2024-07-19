from django.db import models

class Meal(models.Model):
    STARTER = 'ST'
    MAIN_COURSE = 'MC'
    DESSERT = 'DS'
    DRINK = 'DR'
    CATEGORY_CHOICES = [
        (STARTER, 'Starter'),
        (MAIN_COURSE, 'Main Course'),
        (DESSERT, 'Dessert'),
        (DRINK, 'Drink'),
    ]

    name = models.CharField(max_length=50)
    description = models.TextField(max_length=500)
    price = models.DecimalField(max_digits=6, decimal_places=2)
    picture = models.ImageField(upload_to="menu/")
    category = models.CharField(
        max_length=2,
        choices=CATEGORY_CHOICES,
        default=MAIN_COURSE,
    )
    
    def __str__(self):
        return self.name