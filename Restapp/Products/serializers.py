#convert  models.py into Json data to access any device

from rest_framework import serializers
from .models import Product

class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model=Product
        fields = ('id' , 'name' , 'description' , 'price' )