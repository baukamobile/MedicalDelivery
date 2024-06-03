from django.db import models
from django.forms.fields import CharField
from orders.models import Order
# Create your models here.

class PaymentMethod(models.Model):
    payment_method = models.CharField(max_length=10)

class Payment(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    payment_date = models.DateField(auto_now_add=True)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    payment_method = models.ForeignKey(PaymentMethod, on_delete=models.PROTECT)
    status = models.CharField(max_length=100)
    
