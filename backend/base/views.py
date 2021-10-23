# from itertools import product
from itertools import product
from django.shortcuts import render
from django.http import JsonResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .products import products

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
    return Response(products)


@api_view(["GET"])
def getProduct(request, pk):

    product = None

    for i in products:
        if i["_id"] == pk:
            product = i
            break
    """
    # product = map(lambda i: i['_id'] == pk, products)
    # product = map(lambda i: i if i['_id'] == pk else 0 , products)

    product = filter(lambda i: i['_id'] == pk, products)
    product = list(product)
    print(product[0])
    """

    return Response(product)
