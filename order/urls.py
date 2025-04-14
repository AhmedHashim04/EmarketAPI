
from django.urls import path
from .views import OrderListView, OrderDetailView


urlpatterns = [
    path('order/', OrderListView.as_view(), name='order-list'),
    path('order/<int:pk>/', OrderDetailView.as_view(), name='order-detail'),
    path('order/<int:pk>/update/', OrderDetailView.as_view(), name='order-update'),
    path('order/<int:pk>/delete/', OrderDetailView.as_view(), name='order-delete'),

]


