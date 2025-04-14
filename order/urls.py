
from django.urls import path
from .views.order import OrderViewSet
from rest_framework.routers import DefaultRouter


app_name = "order"

router =DefaultRouter()
router.register('my_orders',OrderViewSet,basename='orders')


urlpatterns = router.urls  