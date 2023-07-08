"""
Forms for the shopping cart app
"""
from django import forms


class AddToCartForm(forms.Form):
    """ Form for adding items to the shopping cart """
    quantity = forms.IntegerField(widget=forms.HiddenInput(
        attrs={'class': 'list-inline-item text-right',
               'name': 'product-quantity',
               'id': 'product-quantity',
               'value': '1',
               }))
