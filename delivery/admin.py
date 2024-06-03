from django.contrib import admin
from client.models import Client
from delivery.models import *
from orders.models import *
from payments.models import *
from products.models import *
from users.models import *
# Register your models here.
admin.site.register(Delivery)
admin.site.register(DeliveryPerson)
admin.site.register(Product)
admin.site.register(InventoryProduct)
admin.site.register(Inventory)
admin.site.register(UserTemporary)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(DeliveryAddress)
admin.site.register(Payment)
admin.site.register(PaymentMethod)
admin.site.register(Client)
