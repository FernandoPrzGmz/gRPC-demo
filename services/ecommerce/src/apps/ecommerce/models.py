import uuid
from django.conf import settings
from django.db import models


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return F"{self.name}"


class ShoppingCart(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField('ecommerce.Product', through='ecommerce.ShoppingCartItem')
    
    def __str__(self):
        return F"{self.user}"


class ShoppingCartItem(models.Model):
    product = models.ForeignKey('ecommerce.Product', on_delete=models.CASCADE)
    shopping_cart = models.ForeignKey('ecommerce.ShoppingCart', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    is_enabled = models.BooleanField(default=True)

    def __str__(self):
        return F"{self.product}"
    

class Order(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    items = models.ManyToManyField('ecommerce.Product', through='ecommerce.OrderItem')
    order_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return F"{self.id}"


class OrderItem(models.Model):
    product = models.ForeignKey('ecommerce.Product', on_delete=models.CASCADE)
    order = models.ForeignKey('ecommerce.Order', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()

    def __str__(self):
        return F"{self.product}"
