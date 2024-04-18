from django.db import models
from django.contrib.auth.models import User 

# Create your models here.
class category(models.TextChoices):
    COMPUTER ='Computer'
    FOOD = 'Food'
    KIDS = 'Kids'
    HOME = 'Home'



class product(models.Model):
    name = models.CharField(max_length=200,default="",blank=False)
    discription = models.TextField(max_length=1000,default="",blank=False)
    price = models.DecimalField(max_digits=7,decimal_places=2,default=0)
    brand = models.CharField(max_length=200,default="",blank=False)
    category = models.CharField(max_length=40,choices=category.choices)
    stock=models.IntegerField(default=0)
    user = models.ForeignKey(User , null=True , on_delete=models.SET_NULL)


    def __str__(self):
        return self.name



