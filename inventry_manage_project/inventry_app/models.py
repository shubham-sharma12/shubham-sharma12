from django.contrib.auth.models import AbstractUser
from django.db import models
import uuid

# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True)

class Category(models.Model):
    name = models.CharField(max_length=40)
    
    def __str__(self) -> str:
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=40, blank=False)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="items")    
    created_on = models.DateField(auto_now_add=True)
    updated_on = models.DateField(auto_now=True)

    def __str__(self) -> str:
        return self.name
    

class Stock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.ForeignKey(Item, on_delete=models.CASCADE, related_name='stock')
    quantity = models.PositiveIntegerField()
    
    def __str__(self):        
        return f"Stock of {self.item.name}"