from django.contrib import admin
from .models import productlist


class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price','stock')

admin.site.register(productlist,ProductAdmin)