from django import forms


class AddToCartForm(forms.Form):
    quantity = forms.IntegerField(widget=forms.HiddenInput(
        attrs={'class': 'list-inline-item text-right',
               'name': 'product-quantity',
               'id': 'product-quantity',
               'value': '1',
               }))
    # quantity = forms.IntegerField(widget=QuantityInput)
