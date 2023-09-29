from django.contrib import admin

from .models import *
# Register your models here.

admin.site.register((Maincategory,Subcategory,Brand,Product,Buyer,Wishlist))