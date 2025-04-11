import django_filters
from product.models import Product

class ProductFilter(django_filters.FilterSet):
    class Meta:
        model = Product
        fields = {
            'name': ['exact', 'icontains'],
            'category': ['exact'],
            'price': ['lt', 'gt'],
            'created_at': ['date', 'year__gt'],
        }
        # fields = ( 'category' , 'price', 'created_at') 