from order.models import Order

from django_filters.rest_framework import FilterSet, filters

class OrderFilter(FilterSet):
    order_status = filters.ChoiceFilter(choices=Order.order_status)
    payment_status = filters.ChoiceFilter(choices=Order.payment_status)
    created_at = filters.DateFromToRangeFilter()
    updated_at = filters.DateFromToRangeFilter()

    class Meta:
        model = Order
        fields = {
            'order_status': ['exact'],
            'payment_status': ['exact'],
            'created_at': ['date', 'year__gt'],
            'updated_at': ['date', 'year__gt'],
        }
