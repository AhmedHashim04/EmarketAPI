from django.shortcuts import get_object_or_404
from ..models import Product , Review
from rest_framework.permissions import IsAuthenticated
from rest_framework.decorators import permission_classes ,authentication_classes
from rest_framework_simplejwt.authentication import JWTAuthentication
from ..filters import ReviewsFilter
from ..serializers.review import  ReviewSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

@api_view(['POST'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def create_review(request, product_id):
    try:
        product = get_object_or_404(Product, id=product_id)
    except Product.DoesNotExist:
        return Response({'error': 'Product not found'}, status=404)
    
    serializer = ReviewSerializer(data=request.data)
    # Check if the user has already reviewed this product

    if Review.objects.filter(product=product, user=request.user).exists():
        return Response({'error': 'You have already reviewed this product'}, status=400)
    # Check if the user is the owner of the product
    if product.user == request.user:
        return Response({'error': 'You cannot review your own product'}, status=400)
    
    if serializer.is_valid():
        serializer.save(product=product, user=request.user)
        return Response({'Review': serializer.data}, status=201)
    return Response(serializer.errors, status=400)

@api_view(['PUT'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def update_review(request,product_id,review_id):
    try:
        review = get_object_or_404(Review,product=product_id, id=review_id)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=404)
    
    # Check if the user is the owner of the review
    if review.user != request.user:
        return Response({'error': 'You do not have permission to update this review'}, status=403)
    
    serializer = ReviewSerializer(review, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response({'Review': serializer.data})
    return Response(serializer.errors, status=400)

@api_view(['DELETE'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def delete_review(request,product_id,review_id):
    try:
        review = get_object_or_404(Review,product=product_id, id=review_id)
    except Review.DoesNotExist:
        return Response({'error': 'Review not found'}, status=404)

    if review.user != request.user:
        return Response({'error': 'You do not have permission to update this review'}, status=403)
    
    review.delete()
    return Response(status=204)

@api_view(['GET'])
@authentication_classes([JWTAuthentication])
@permission_classes([IsAuthenticated])
def user_reviews(request):
    paginator = PageNumberPagination()
    paginator.page_size = 1  # /api/products/?page=1 to get 10 products per page
    filterset = ReviewsFilter(request.GET, queryset=Review.objects.filter(user=request.user).order_by('?'))    # /api/products/?category=Food  to filter by category
    queryset = paginator.paginate_queryset(filterset.qs, request)
    serializer = ReviewSerializer(queryset, many=True)
    return Response({'Reviews': serializer.data, 'count':filterset.qs.count()} )
    
