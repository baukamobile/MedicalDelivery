from django.db import models
from orders.models import Order
# Create your models here.
from django.core.validators import RegexValidator

class DeliveryPerson(models.Model):
    # Add fields relevant to a delivery person
    name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    # Add any other fields you need, such as address, profile picture, etc.

    def __str__(self):
        return self.name

class Delivery(models.Model):
    order_id = models.ForeignKey(Order, on_delete=models.PROTECT)
    delivery_person = models.ForeignKey(DeliveryPerson, on_delete=models.CASCADE)
    delivery_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=100) #пока не трогать ему. Не знаем с кем можно
    #соединить
    phone_regex = RegexValidator(
           regex=r'^\+?1?\d{9,11}$',
           message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed."
       )
    tracking_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    
    def __str__(self):
        return f"Delivery for Order #{self.order_id} by {self.delivery_person.name}"



