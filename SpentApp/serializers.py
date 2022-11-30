from rest_framework import serializers
from SpentApp.models import Product


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('ProductId', 'ProductName', 'ProductAmount', 'ProductPrice', 'ProductTotalPrice', 'Date')
