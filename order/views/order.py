from ..models import Order
from ..serializers.order import OrderSerializer
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated 
from rest_framework_simplejwt.authentication import JWTAuthentication
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet
from rest_framework.pagination import PageNumberPagination
from django_filters.rest_framework import DjangoFilterBackend
from ..filters import OrderFilter
from rest_framework import status


class OrderViewSet(ModelViewSet):
    serializer_class = OrderSerializer
    permission_classes = [IsAuthenticated]
    authentication_classes = [JWTAuthentication]
    filter_backends = (DjangoFilterBackend,)
    filterset_class = OrderFilter
    pagination_class = PageNumberPagination

    def get_queryset(self):
        # Filter orders by the authenticated user
        return Order.objects.filter(user=self.request.user)





# class OrderListView(generics.ListCreateAPIView):
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]

#     def get_queryset(self):
#         # Filter orders by the authenticated user
#         return Order.objects.filter(user=self.request.user)
    
#     def get(self, request, *args, **kwargs):
#         orders = self.get_queryset()
#         serializer = self.get_serializer(orders, many=True)
#         return Response(serializer.data)
    
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         if serializer.is_valid():
#             # Link the order to the authenticated user
#             serializer.save(user=request.user)
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# class OrderDetailView(generics.RetrieveUpdateDestroyAPIView,):
#     serializer_class = OrderSerializer
#     permission_classes = [IsAuthenticated]
#     # authentication_classs = [JWTAuthentication]


#     def get_queryset(self):
#         # Ensure the user can only access their own orders
#         return Order.objects.filter(user=self.request.user)
    
#     def get(self, request, *args, **kwargs):
#         order = self.get_object()
#         serializer = self.get_serializer(order)
#         return Response(serializer.data)
    
#     def put(self, request, *args, **kwargs):
#         order = self.get_object()
#         serializer = self.get_serializer(order, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, *args, **kwargs):
#         order = self.get_object()
#         order.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

    