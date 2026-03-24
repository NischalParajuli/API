from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Category(models.Model):
    name = models.CharField(max_length=15)

class Food(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=8, decimal_places=2)
    available = models.BooleanField(default=True)

class table(models.Model):
    table_number = models.CharField(max_length=2)
    is_available = models.BooleanField(default=False, null=True, blank=True)

class Order(models.Model):
    user = models.ForeignKey(User,max_length=50,on_delete=models.CASCADE )
    total_price = models.DecimalField(null = True ,  blank= True , max_digits=4 ,  decimal_places= 2)
    
class OrderItem(models.Model): # Junction Table ... Many To Many Relationship
    order = models.ForeignKey(Order,on_delete=models.PROTECT)
    food = models.ForeignKey(Food,on_delete=models.PROTECT)
