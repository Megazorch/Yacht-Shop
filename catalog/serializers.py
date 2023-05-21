from .models import CartLineItem, Cart
from rest_framework import serializers


class CartLineItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CartLineItem
        fields = ['id', 'quantity', 'owner']

