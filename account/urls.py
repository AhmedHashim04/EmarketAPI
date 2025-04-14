
from django.urls import path , include
from .views import register ,login, logout_view ,ProfileView ,forget_password , reset_password

app_name = 'account'
urlpatterns = [
    path('',register , name='register'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', ProfileView.as_view(), name='profile-update'),
    path('forget-password/', forget_password, name='forget_password'),
    path('reset-password/<str:token>/', reset_password, name='reset_password'),
    path('', include('rest_framework.urls')),




]
