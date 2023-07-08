"""
Definition of views.
"""
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views import generic
from rest_framework import generics, permissions

from catalog import models, forms, serializers
from .permissions import IsOwnerOrReadOnly


def index(request):
    """View function for home page of site."""

    # Generate counts of some main objects
    num_yachts = models.Yacht.objects.all().count()
    yachts = models.Yacht.objects.order_by('-price')[:3]

    context = {
        'num_yachts': num_yachts,
        'yachts': yachts,
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)


class AboutView(generic.TemplateView):
    """ About page view class """
    template_name = 'about.html'


class ContactView(generic.TemplateView):
    """ Contact page view class """
    template_name = 'contact.html'


class YachtListView(generic.ListView):
    """ Yacht list view class """
    model = models.Yacht
    template_name = 'shop.html'  # Specify your own template name/location

    def get_queryset(self):     # ChatGPT
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category', )

        # Filter the queryset based on the category_id
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset

    def get_context_data(self, **kwargs):       # ChatGPT
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context


class YachtDetailView(generic.DetailView):
    """ Yacht detail view class """

    def get(self, request, *args, **primary_key):
        """ Instruction for GET request
        :param request:
        :return:
        """
        yacht = models.Yacht.objects.get(pk=primary_key['primary_key'])
        form = forms.AddToCartForm()
        return render(request, 'yacht-detail.html',
                      {'yacht': yacht, 'form': form})

    @staticmethod
    def post(request, primary_key):
        """ Instruction for POST request
        :param request:
        :param primary_key:
        :return:
        """
        yacht = models.Yacht.objects.get(pk=primary_key)
        form = forms.AddToCartForm(request.POST)

        if form.is_valid():
            quantity = form.cleaned_data['quantity']
            # Perform necessary actions to add yacht to cart
            # For example, create or update Cart and CartItem objects
            # based on the selected quantity and yacht details

            # Get the user's cart, or create a new one if it doesn't exist
            if not request.user.is_authenticated:
                return redirect('/accounts/login')

            cart, created = models.Cart.objects.get_or_create(user=request.user)    # pylint: disable=unused-variable

            # Check if the yacht is already in the cart
            try:
                cart_item = models.CartLineItem.objects.get(cart=cart, yacht=yacht)
                cart_item.quantity += quantity  # Update quantity if yacht already exists
                cart_item.save()
            except models.CartLineItem.DoesNotExist:
                cart_item = models.CartLineItem(
                    cart=cart, yacht=yacht, quantity=quantity, owner=request.user)
                cart_item.save()

            cart_path = 'cart/' + str(cart.id)

            return redirect(cart_path)  # Redirect to cart view

        return render(request, 'yacht-detail.html',
                          {'yacht': yacht, 'form': form})

    def get_context_data(self, **kwargs):       # ChatGPT
        """ Get context data for yacht shop view
        :param kwargs:
        :return:
        """
        context = super().get_context_data(**kwargs)
        context['categories'] = models.Category.objects.all()
        return context


class CartDetailView(generic.DetailView):
    """ Cart detail view class """
    model = models.Cart
    form = forms.AddToCartForm()
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):       # ChatGPT
        context = super().get_context_data(**kwargs)
        final_price = 0
        cart_id = self.kwargs['pk']
        # Get the cart items and calculate the final price
        id_of_cart = models.Cart.objects.get(pk=cart_id)
        cart_items = models.CartLineItem.objects.filter(cart=id_of_cart)

        for item in cart_items:
            final_price += item.total_price()

        context['cart_items'] = cart_items
        context['final_price'] = final_price
        return context


class SignUpView(generic.CreateView):
    """ Sign up view class """
    form_class = UserCreationForm
    success_url = reverse_lazy("login")
    template_name = "registration/sign-up.html"


# SERIALIZERS
class CartLineItemList(generics.ListCreateAPIView):
    """
    List all code cart line items, or create a new cart line item.
    """
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    queryset = models.CartLineItem.objects.all()
    serializer_class = serializers.CartLineItemSerializer

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)


class CartLineItemDetail(generics.RetrieveUpdateDestroyAPIView):
    """
    Retrieve, update or delete a code cart line item.
    """
    queryset = models.CartLineItem.objects.all()
    serializer_class = serializers.CartLineItemSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly,
                          IsOwnerOrReadOnly]

# END SERIALIZER
