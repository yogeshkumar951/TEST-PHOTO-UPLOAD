from email.policy import default
from unicodedata import name
from django.db import models

# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=20)
    color = models.CharField(max_length=20)
    description = models.CharField(max_length=20)
    price = models.DecimalField(max_digits=6,decimal_places=2)
    image = models.ImageField(upload_to ='image/',default=None)
     
    def __str__(self):
        return self.name
     