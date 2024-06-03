from django.db import models
from customer.models import Customer

class Inventory(models.Model):
    location = models.CharField(max_length=100)
    products = models.ManyToManyField('Product', through='InventoryProduct')

    def __str__(self):
        return f"Location: {self.location}"

class Product(models.Model):
    name = models.CharField(max_length=150)
    description = models.TextField(max_length=200)
    price = models.DecimalField(max_digits=10, decimal_places=2)
    customer_id = models.ForeignKey(Customer, on_delete=models.PROTECT)
    stock_quantity = models.IntegerField()
    expire_date = models.DateField()

    def __str__(self):
        return self.name

class InventoryProduct(models.Model):
    inventory = models.ForeignKey(Inventory, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    stock_quantity = models.IntegerField()

    def __str__(self):
        return f"Inventory: {self.inventory}, Product: {self.product}"
