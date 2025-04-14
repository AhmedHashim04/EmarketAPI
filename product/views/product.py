from django.shortcuts import get_object_or_404
from ..filters import ProductFilter
from rest_framework.pagination import PageNumberPagination
from ..models import Product , Review
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes
from ..serializers.review import  ReviewSerializer

from ..serializers.product import ProductSerializer 
from rest_framework.response import Response
from rest_framework.decorators import api_view

@api_view(['GET'])
def product_list(request):
    paginator = PageNumberPagination()
    paginator.page_size = 1  # /api/products/?page=1 to get 10 products per page
    filterset = ProductFilter(request.GET, queryset=Product.objects.all().order_by('?'))    # /api/products/?category=Food  to filter by category

    queryset = paginator.paginate_queryset(filterset.qs, request)
    
    serializer = ProductSerializer(queryset, many=True)
    return Response({'Products':serializer.data , 'count':filterset.qs.count()} )

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def product_detail(request, product_id):
    try:
        product = get_object_or_404(id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)
    
    serializer = ProductSerializer(product)
    reviews = Review.objects.filter(product=product)
    review_serializer = ReviewSerializer(reviews, many=True)
    return Response({'Product': serializer.data, 'Reviews': review_serializer.data})

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_product(request):
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Product': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)
    
    # Check if the user is the owner of the product
    if product.user != request.user:
        return Response({'error': 'You do not have permission to update this product'}, status=403)
    
    serializer = ProductSerializer(product, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Product': serializer.data})
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)

    if product.user != request.user:
        return Response({'error': 'You do not have permission to update this product'}, status=403)
    
    product.delete()
    return Response(status=204)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_products(request):
    products = Product.objects.filter(user=request.user)
    serializer = ProductSerializer(products, many=True)
    return Response({'Products': serializer.data})
