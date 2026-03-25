from django.db import models
from django.contrib.auth import get_user_model
User = get_user_model()
# from django.contrib.auth.models import User
# Create your models here.
class Category(models.Model):
   name = models.CharField(max_length=15)     # Breakfast, Lunch, Dinner, Drinks
   def __str__(self):
      return self.name

class Food(models.Model):
   name = models.CharField(max_length=100)   # abc, xyz
   price = models.IntegerField()
   category = models.ForeignKey(Category, on_delete=models.CASCADE)   # Breakfast
   
   def __str__(self):
      return f"{self.name} - {self.price}"

class Table(models.Model):
   number = models.CharField(max_length=2)
   is_available = models.BooleanField(default=False, null=True, blank=True)
   
   def __str__(self):
      return f"Table no. {self.number} - {self.is_available}"

class Order(models.Model):
   status_choice = [
      ('Complete',"Complete"),
      ('Pending','Pending'),
      ('Delivered','Delivered')
   ]
   user = models.ForeignKey(User, on_delete=models.CASCADE)
   total_price = models.IntegerField(null=True, blank=True)
   status = models.CharField(max_length=10, choices=status_choice, default="Pending", null=True, blank=True)
   
   def __str__(self):
      return f"{self.user} - {self.total_price}"

class OrderItem(models.Model):
   order = models.ForeignKey(Order,on_delete=models.PROTECT)
   food = models.ForeignKey(Food, on_delete=models.PROTECT)