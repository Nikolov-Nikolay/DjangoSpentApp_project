from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from SpentApp.models import Product
from SpentApp.serializers import ProductSerializer

from django.core.files.storage import default_storage


# Create your views here.

@csrf_exempt
def productapi(request, id=0):
    if request.method == 'GET':
        product = Product.objects.all()
        product_serializer = ProductSerializer(product, many=True)
        return JsonResponse(product_serializer.data, safe=False)
    elif request.method == 'POST':
        product_data = JSONParser().parse(request)
        product_serializer = ProductSerializer(data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse('Added Successfully', safe=False)
        return JsonResponse('Failed to add', safe=False)
    elif request.method == 'PUT':
        product_data = JSONParser().parse(request)
        product = Product.objects.get(ProductId=product_data['ProductId'])
        product_serializer = ProductSerializer(product, data=product_data)
        if product_serializer.is_valid():
            product_serializer.save()
            return JsonResponse('Update Successfully', safe=False)
        return JsonResponse('Failed to update')
    elif request.method == 'DELETE':
        product = Product.objects.get(ProductId=id)
        product.delete()
        return JsonResponse('Deleted Successfully', safe=False)
