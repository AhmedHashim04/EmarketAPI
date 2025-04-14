from django.db import models
from account.models import User ,Profile
from product.models import Product
# Create your models here.

class OrderStatus(models.TextChoices):
    PENDING = 'Pending', 'Pending'
    SHIPPED = 'Shipped', 'Shipped'
    DELIVERED = 'Delivered', 'Delivered'
    CANCELLED = 'Cancelled', 'Cancelled'

class PaymentStatus(models.TextChoices):
    PAIED ='Paid'
    UNPAID = 'Unpaid'

class PaymentMethod(models.TextChoices):
    COD = 'Cash on Delivery'
    CARD = 'Credit/Debit Card'
    PAYPAL = 'PayPal'
    BANK_TRANSFER = 'Bank Transfer'


class Order(models.Model):
    
    city = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    postal_code = models.CharField(max_length=20)
    phone_number = models.CharField(max_length=15)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100)
    profile = models.ForeignKey(Profile, on_delete=models.CASCADE)
    order_date = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=20, choices=OrderStatus.choices, default=OrderStatus.PENDING)
    payment_status = models.CharField(max_length=20, choices=PaymentStatus.choices, default=PaymentStatus.UNPAID)
    payment_method = models.CharField(max_length=20, choices=PaymentMethod.choices, default=PaymentMethod.COD)
    total_amount = models.DecimalField(max_digits=10, decimal_places=2)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    created_at = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return f"Order {self.pk} - {self.user.username}"
    
class OrderItem(models.Model):
    order = models.ForeignKey(Order, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.product.name} (x{self.quantity})"
    def get_total_price(self):
        return self.price * self.quantity
