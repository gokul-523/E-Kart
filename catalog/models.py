from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone

# Item Model
class Item(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Sold', 'Sold'),
    ]

    name = models.CharField(max_length=255)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    category = models.CharField(max_length=100)  # Free-form category field
    image = models.CharField(max_length=255)  # Text field for image path
    status = models.CharField(max_length=50, choices=STATUS_CHOICES, default='Available')
    added_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

# Cart Model
class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='carts')
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    def __str__(self):
        return f"{self.item.name} - {self.user.username}"

# Order Model
class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='orders')
    order_date = models.DateTimeField(auto_now_add=True)
    is_completed = models.BooleanField(default=False)

    def __str__(self):
        return f"Order {self.id} by {self.user.username}"

# OrderItem Model
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='order_items', on_delete=models.CASCADE)
    item = models.ForeignKey(Item, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return f"{self.quantity} of {self.item.name} in order {self.order.id}"
