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


class ShopOptionForm(forms.Form):
    """ Form for selecting a shop option """
    CHOICES = [('option1', 'A to Z'), ('option2', 'Cheap to Expensive'),
               ('option3', 'Expensive to Cheap'), ('option4', 'Newest to Oldest'),
               ('option5', 'Oldest to Newest')]

    shop_option = forms.ChoiceField(
        choices=[
            ('option1', 'A to Z'),
            ('option2', 'Cheap to Expensive'),
            ('option3', 'Expensive to Cheap'),
            ('option4', 'Newest to Oldest'),
            ('option5', 'Oldest to Newest')],
        widget=forms.Select(attrs={'class': 'form-control'}))
