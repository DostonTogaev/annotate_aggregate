from django.db import models

# Create your models here.

class Category(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    price = models.FloatField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)

class Customer(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name
class Order(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    sel_data = models.DateTimeField()

