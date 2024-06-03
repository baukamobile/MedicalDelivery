from django.db import models
from users.models import UserTemporary
from django.core.validators import RegexValidator
# Create your models here.
class Client(models.Model):
    # user = models.OneToOneField('UserTemporary', on_delete=models.CASCADE, \
    #     # related_name='client'
    # )
    name = models.CharField(max_length=100)
    surname = models.CharField(max_length=100)
    phone_regex = RegexValidator(
           regex=r'^\+?1?\d{9,11}$',
           message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed."
       )
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    address = models.CharField(max_length=100)
    balance = models.DecimalField(max_digits=10, decimal_places=2)
