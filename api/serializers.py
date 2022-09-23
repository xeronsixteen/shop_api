from django.contrib.auth import get_user_model
from rest_framework import serializers

from webapp.models import Product, OrderProduct, Order


class UserModelsSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ('username', 'email', 'id')


class ProductModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = '__all__'


class OrderProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = OrderProduct
        fields = ('id', 'order', 'product', 'qty')


class OrderSerializer(serializers.ModelSerializer):
    user = UserModelsSerializer
    order_products = OrderProductSerializer(many=True, read_only=True)

    class Meta:
        model = Order
        fields = "__all__"
