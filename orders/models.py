from django.db import models
from users.models import UserTemporary
from products.models import Product

class Order(models.Model):
    user_id = models.ForeignKey(UserTemporary, on_delete=models.PROTECT)
    order_date = models.DateField(auto_now_add=True)
    status = models.CharField(max_length=100)
    # Instead of ForeignKey, use a OneToOneField to link to the delivery address
    delivery_address = models.OneToOneField('DeliveryAddress', on_delete=models.CASCADE)

    def __str__(self):
        return f"User: {self.user_id}, Date: {self.order_date}, Status: {self.status}"

class DeliveryAddress(models.Model):
    # Link the delivery address to a specific user
    user = models.ForeignKey(UserTemporary, on_delete=models.CASCADE)
    address = models.CharField(max_length=100)

    def __str__(self):
        return f"User: {self.user}, Address: {self.address}"

class OrderItem(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    product_id = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"Order: {self.order_id}, Product: {self.product_id}, Quantity: {self.quantity}, Price: {self.price}"
