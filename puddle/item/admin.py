from django.contrib import admin

# Import your models from the models.py file
from .models import Category, Item 

# Register your models here
admin.site.register(Category)
admin.site.register(Item)