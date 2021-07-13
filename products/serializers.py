from rest_framework import serializers
from products.models import *

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Image
        fields = ('name','image_url')

class BestItemSerializer(serializers.ModelSerializer):
    images= ImageSerializer(many=True,read_only=True)
    class Meta:
        model = Product
        fields = ('id','name','price','images',)
    