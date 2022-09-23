from rest_framework import serializers

from webapp.models import Product


class ProductModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
