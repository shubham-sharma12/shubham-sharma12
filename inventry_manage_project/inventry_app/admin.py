from django.contrib import admin
from .models import Category, Item, Stock, User

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Item)
admin.site.register(Stock)
