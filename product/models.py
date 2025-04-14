from django.db import models
from django.contrib.auth.models import User
import uuid

# class Category(models.Model):
#     name = models.CharField(max_length=50, choices=Category.choices, unique=True)

#     def __str__(self):
#         return self.name

class Brand(models.TextChoices):
    APPLE = 'Apple', 'Apple'
    SAMSUNG = 'Samsung', 'Samsung'
    SONY = 'Sony', 'Sony'
    LG = 'LG', 'LG'
    NIKE = 'Nike', 'Nike'
    ADIDAS = 'Adidas', 'Adidas'
    PUMA = 'Puma', 'Puma'
    UNDER_ARMOUR = 'Under Armour', 'Under Armour'
    REEBOK = 'Reebok', 'Reebok'
    MICROSOFT = 'Microsoft', 'Microsoft'
    GOOGLE = 'Google', 'Google'
    AMAZON = 'Amazon', 'Amazon'
    FACEBOOK = 'Facebook', 'Facebook'
    TESLA = 'Tesla', 'Tesla'
    HUAWEI = 'Huawei', 'Huawei'
    XIAOMI = 'Xiaomi', 'Xiaomi'
    LENOVO = 'Lenovo', 'Lenovo'
    DELL = 'Dell', 'Dell'
    HP = 'HP', 'HP'
    ASUS = 'Asus', 'Asus'

class Category(models.TextChoices):
    TOYS = 'Toys', 'Toys'
    FOOD = 'Food', 'Food'
    ELECTRONICS = 'Electronics', 'Electronics'
    FASHION = 'Fashion', 'Fashion'
    HOME = 'Home', 'Home'
    BEAUTY = 'Beauty', 'Beauty'
    BOOKS = 'Books', 'Books'
    SPORTS = 'Sports', 'Sports'
    HEALTH = 'Health', 'Health'


class Product(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=40, blank=False, choices=Brand.choices, default=Brand.APPLE)
    category = models.CharField(max_length=40, blank=False, choices=Category.choices, default=Category.TOYS)
    # category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='products', null=True)
    image = models.ImageField(upload_to='products/', default='products/default.jpg')
    stock = models.IntegerField()
    rating = models.DecimalField(max_digits=3, decimal_places=2, default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, on_delete=models.SET_NULL, related_name='products', null=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if not (0 <= self.rating <= 5):
            raise ValidationError({'rating': 'Rating must be between 0 and 5.'})

    def __str__(self):
        """
        Returns the string representation of the Product instance,
        which is the name of the product.
        """
        return self.name

class Review(models.Model):
    id = models.UUIDField(primary_key=True, editable=False, default=uuid.uuid4)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews', null=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews',null=True)
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

