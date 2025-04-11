from django.db import models
from django.contrib.auth.models import User

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
    name = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    brand = models.CharField(max_length=200, blank=False)
    category = models.CharField(max_length=40, blank=False, choices=Category.choices, default=Category.TOYS)
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
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='reviews')
    rating = models.DecimalField(max_digits=3, decimal_places=2)
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def clean(self):
        from django.core.exceptions import ValidationError
        if not (0 <= self.rating <= 5):
            raise ValidationError({'rating': 'Rating must be between 0 and 5.'})