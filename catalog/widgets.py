"""
Widgets for the catalog app
"""
from django.forms.widgets import NumberInput


class QuantityInput(NumberInput):
    """ Widget for quantity input """
    template_name = 'catalog/widgets/quantity_input.html'
    input_type = 'number'
    min_value = 1
    max_value = 10
    step = 1
