# from itertools import product
# from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Product
from .serializers import ProductSerializer

# Create your views here.


@api_view(["GET"])
def getRoutes(request):
    routes = [
        "/api/products/",
        "/api/products/create",
        "/api/products/uploald/",
        "/api/",
    ]
    return Response(routes)


@api_view(["GET"])
def getProducts(request):
    products = Product.objects.all()
    serializers = ProductSerializer(products, many=True)
    return Response(serializers.data)


@api_view(["GET"])
def getProduct(request, pk):

    product = Product.objects.get(_id=pk)
    serializer = ProductSerializer(product, many=False)

    return Response(serializer.data)
