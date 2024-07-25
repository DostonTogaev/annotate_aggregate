from calendar import Month

from django.contrib import admin

from app.models import Product, Category, Order, Customer

# Register your models here.


admin.site.register(Product)
admin.site.register(Category)
admin.site.register(Order)
admin.site.register(Customer)