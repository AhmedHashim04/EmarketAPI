
from django.urls import path
from .views import register ,login, logout_view ,ProfileView

app_name = 'account'
urlpatterns = [
    path('/',register , name='register'),
     path('login/', login, name='login'),
     path('logout/', logout_view, name='logout'),
    path('profile/<int:pk>/', ProfileView.as_view(), name='profile'),
    path('profile/<int:pk>/update/', ProfileView.as_view(), name='profile-update'),

]
