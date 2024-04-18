from django.shortcuts import get_object_or_404,render
from rest_framework.decorators import api_view , permission_classes
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from .models import product
from .serializers import ProductSerializer
# Create your views here.

@api_view(['GET'])
def get_all_product(request):
    products = product.objects.all()
    serializer = ProductSerializer(products, many=True)
    print(products)
    return Response({"products":serializer.data})


@api_view(['GET'])
def get_product(request,pk):
    products = get_object_or_404(product,id=pk)
    serializer = ProductSerializer(products, many=False)
    print(products)
    return Response({"product":serializer.data})



@api_view(['POST'])
@permission_classes([IsAuthenticated])
def new_product(request):
    data = request.data
    serializer = ProductSerializer(data = data)
    if serializer.is_valid():
       products = product.objects.create(**data,user=request.user)
       res = ProductSerializer(products,many=False)
       return Response({"product":res.data})
    
    else:
        return Response(serializer.errors)
    

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update_product(request,pk):
    Product = get_object_or_404(product,id=pk)
    if Product.user != request.user:
        return Response({"error":"sorry you can not update"})
    
    else:
        Product.name = request.data["name"],
        Product.discription = request.data["discription"],
        Product.price = request.data["price"],
        Product.brand = request.data["brand"],
        Product.category = request.data["category"],
        Product.stock = request.data["stock"]

        Product.save()
        serializer = ProductSerializer(Product,many=False)
        return Response({"product":serializer.data})



@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_product(request,pk):
    Product = get_object_or_404(product,id=pk)
    if Product.user != request.user:
        return Response({"error":"sorry you can not update"})
    
    else:
       
        Product.delete()
        return Response({"details":"deleted"})


       
    