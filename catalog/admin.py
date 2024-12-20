from django.contrib import admin
from .models import Item, Order,Cart , OrderItem

admin.site.register(Item)
admin.site.register(Order)

admin.site.register(Cart)

admin.site.register(OrderItem)