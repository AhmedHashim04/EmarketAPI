from django.shortcuts import get_object_or_404
from ..models import Product , Review
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes ,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..serializers.product import ProductSerializer  
from ..serializers.review import ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view



@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_products(request):
    products = Product.objects.filter(user=request.user)
    serializer = ProductSerializer(products, many=True)
    return Response({'Products': serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_reviewed_products(request):
    reviews = Review.objects.filter(user=request.user)
    product_ids = reviews.values_list('product__id', flat=True)
    products = Product.objects.filter(id__in=product_ids)
    serializer = ProductSerializer(products, many=True)
    return Response({'Products': serializer.data})

@api_view(['GET'])
@permission_classes([IsAuthenticated])
@authentication_classes([JWTAuthentication])
def user_reviewed_product(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)
    
    reviews = Review.objects.filter(product=product, user=request.user)
    serializer = ReviewSerializer(reviews, many=True)
    return Response({'Reviews': serializer.data})
