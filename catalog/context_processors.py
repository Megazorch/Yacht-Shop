"""
This module is used to create a context processor for the cart_id and retrieve total amount of items in the cart.
"""
from catalog import models


def cart_id(request):
    """ This function is used to retrieve the cart_id of the user and retrieve total amount of items in the cart.
    :param request:
    :return:
    """
    cart_id = None
    total_amount_of_items_in_cart = 0

    if request.user.is_authenticated:
        cart_id = request.user.cart.id  # Assuming the cart ID is accessible through request.user.cart

    cart_items = models.CartLineItem.objects.filter(cart=cart_id)

    for item in cart_items:
        total_amount_of_items_in_cart += item.quantity

    return {'card_id': cart_id, 'total_amount_of_items_in_cart': total_amount_of_items_in_cart}


def categories_for_footer(request):
    """
    This function is used to retrieve the list of all categories.
    :param request:
    :return:
    """
    list_of_categories = models.Category.objects.all()
    return {'list_of_categories': list_of_categories}