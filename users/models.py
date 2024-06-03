from django.db import models
from django.db.backends.utils import datetime
from django.db.models.enums import Choices
from django.db.models.query import DateField
from django.core.validators import RegexValidator

# Create your models here.
class UserTemporary(models.Model):  #временный user
    # user_id = models.IntegerField() #unneccesary
    USER_TYPE_CHOICES = (
            ('Customer', 'Customer'),
            ('Admin', 'Admin'),
            ('DeliveryPerson', 'DeliveryPerson'),
            ('Client', 'Client'),

            # ('UserTemporary)
        )
    username = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    full_name = models.CharField(max_length=100)
    phone_regex = RegexValidator(
           regex=r'^\+?1?\d{9,11}$',
           message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed."
       )
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    phone_number = models.CharField(max_length=100)
    address = models.CharField(max_length=100)
    user_type = models.CharField(max_length=100, choices=USER_TYPE_CHOICES)
    join_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.username
