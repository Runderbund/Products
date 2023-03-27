from rest_framework import serializers
from .models import Car

class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ['title', 'description', 'price', 'inventory_quantity']