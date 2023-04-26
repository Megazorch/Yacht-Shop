from .models import *
from django.views import generic
from django.shortcuts import render, redirect
from django.views import View
from .forms import AddToCartForm


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
    def get(self, request, pk):
        yacht = Yacht.objects.get(pk=pk)
        form = AddToCartForm()
        return render(request, 'yacht-detail.html', {'yacht': yacht, 'form': form})

    def post(self, request, pk):
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
                cart_item = CartLineItem(cart=cart, yacht=yacht, quantity=quantity)
                cart_item.save()

            cart_path = 'cart/' + str(cart.id)

            return redirect(cart_path)  # Redirect to cart view
        else:
            return render(request, 'yacht-detail.html', {'yacht': yacht, 'form': form})


class CartDetailView(generic.DetailView):
    model = Cart
    template_name = 'cart.html'

    def get_context_data(self, **kwargs):       # ChatGPT
        context = super().get_context_data(**kwargs)
        final_price = 0
        cart_items = CartLineItem.objects.filter(cart=2)

        for item in cart_items:
            final_price += item.total_price()

        context['cart_items'] = cart_items
        context['final_price'] = final_price
        return context

