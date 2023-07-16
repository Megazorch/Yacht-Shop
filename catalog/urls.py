"""
This module contains the urls for the yacht_shop app.
"""
from django.urls import path, include
import debug_toolbar
from rest_framework.urlpatterns import format_suffix_patterns
from . import views

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.

urlpatterns = [
    path(
        '',
        views.index,
        name='index'),
    path(
        'yachts/',
        views.YachtListView.as_view(),
        name='shop'),
    path(
        'yachts/<int:primary_key>',
        views.YachtDetailView.as_view(),
        name='yacht-detail'),
    path(
        '__debug__/',
        include(
            debug_toolbar.urls)),
    path(
        'yachts/cart/<int:pk>',
        views.CartDetailView.as_view(),
        name='cart'),
    path(
        'cart-line-items/',
        views.CartLineItemList.as_view()),
    path(
        'cart-line-items/<int:pk>/',
        views.CartLineItemDetail.as_view()),
    path(
        "accounts/sign-up/",
        views.SignUpView.as_view(),
        name="sign-up"),
    path(
        'about/',
        views.AboutView.as_view(),
        name='about'),
    path(
        'contact/',
        views.ContactView.as_view(),
        name='contact'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
