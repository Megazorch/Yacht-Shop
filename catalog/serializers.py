"""
Serializers for the cart app
"""
from rest_framework import serializers
from .models import CartLineItem


class CartLineItemSerializer(serializers.ModelSerializer):
    """ Serializer for CartLineItem model """
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = CartLineItem
        fields = ['id', 'quantity', 'owner']
