from rest_framework import serializers
from products.models import *

class ImageSerializer(serializers.ModelSerializer):
    image_classification = serializers.SerializerMethodField()
    def get_image_classification(self,object):
        return object.image_classification.name
    class Meta:
        model = Image
        fields = ('image_url','image_classification')

class BestItemSerializer(serializers.ModelSerializer):
    images = ImageSerializer(many=True,read_only=True)
    product_stocks = serializers.SerializerMethodField()

    def get_product_stocks(self,object):
        product_stocks = [{
            'size' :product_detail.size.name,
            'stock':product_detail.stock} for product_detail in object.productdetail_set.all()]
        return product_stocks
    class Meta:
        model = Product
        fields = ('id','name','price','images','product_stocks')

    