from .models import *
from django.views import generic
from django.shortcuts import render, redirect
from django.views import View
from .forms import *
from catalog.models import CartLineItem
from catalog.serializers import *
from rest_framework import generics
from django.contrib.auth.models import User

from .permissions import IsOwnerOrReadOnly


def index(request):
    """View function for home page of site."""

    # Generate counts of some main objects
    num_yachts = Yacht.objects.all().count()
    yachts = Yacht.objects.order_by('-price')[:3]

    context = {
        'num_yachts': num_yachts,
        'yachts': yachts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class AboutView(generic.TemplateView):
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    template_name = 'contact.html'


class YachtListView(generic.ListView):
    model = Yacht
    template_name = 'shop.html'  # Specify your own template name/location

    def get_queryset(self):     # ChatGPT
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')

        # Filter the queryset based on the category_id
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

    def get_context_data(self, **kwargs):       # ChatGPT
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class YachtDetailView(View):
    @staticmethod
    def get(request, pk):
        yacht = Yacht.objects.get(pk=pk)
        form = AddToCartForm()
        return render(request, 'yacht-detail.html', {'yacht': yacht, 'form': form})

    @staticmethod
    def post(request, pk):
        yacht = Yacht.objects.get(pk=pk)
        form = AddToCartForm(request.POST)
        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            # Perform necessary actions to add yacht to cart
            # For example, create or update Cart and CartItem objects
            # based on the selected quantity and yacht details

            # Get the user's cart, or create a new one if it doesn't exist
            cart, created = Cart.objects.get_or_create(user=request.user)

            # Check if the yacht is already in the cart
            try:
                cart_item = CartLineItem.objects.get(cart=cart, yacht=yacht)
                cart_item.quantity += quantity  # Update quantity if yacht already exists
                cart_item.save()
            except CartLineItem.DoesNotExist:
                cart_item = CartLineItem(cart=cart, yacht=yacht, quantity=quantity, owner=request.user)
                cart_item.save()

            cart_path = 'cart/' + str(cart.id)

            return redirect(cart_path)  # Redirect to cart view
        else:
            return render(request, 'yacht-detail.html', {'yacht': yacht, 'form': form})

    def get_context_data(self, **kwargs):       # ChatGPT
        context = super().get_context_data(**kwargs)
        context['categories'] = Category.objects.all()
        return context


class CartDetailView(generic.DetailView):
    model = Cart
    form = AddToCartForm()
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):       # ChatGPT
        context = super().get_context_data(**kwargs)
        final_price = 0
        cart_id = self.kwargs['pk']
        # Get the cart items and calculate the final price
        id = Cart.objects.get(pk=cart_id)
        cart_items = CartLineItem.objects.filter(cart=id)

        for item in cart_items:
            final_price += item.total_price()

        context['cart_items'] = cart_items
        context['final_price'] = final_price
        return context


# SERIALIZERS
from rest_framework import permissions


class CartLineItemList(generics.ListCreateAPIView):
    """
    List all code cart line items, or create a new cart line item.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = CartLineItem.objects.all()
    serializer_class = CartLineItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CartLineItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code cart line item.
    """
    queryset = CartLineItem.objects.all()
    serializer_class = CartLineItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

# END SERIALIZER