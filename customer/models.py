from django.db import models
from django.core.validators import RegexValidator

from users.models import UserTemporary
# Create your models here.
class Customer(models.Model):
    name = models.OneToOneField(UserTemporary, on_delete=models.CASCADE)
    address = models.CharField(max_length=40)
    phone_regex = RegexValidator(
           regex=r'^\+?1?\d{9,11}$',
           message="Phone number must be entered in the format: '+999999999'. Up to 11 digits allowed."
       )
    phone_number = models.CharField(validators=[phone_regex], max_length=11, blank=True)
    email = models.CharField(max_length=40)
    license_number = models.CharField(max_length=100)
