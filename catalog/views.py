from django.db.models import Q
from django.http import request
from django.shortcuts import render
from .models import *
from django.views import generic


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
    #context_object_name = 'yachts'

    def get_queryset(self):     # ChatGPT
        queryset = super().get_queryset()
        category_id = self.request.GET.get('category')

        # Filter the queryset based on the category_id
        if category_id:
            queryset = queryset.filter(category__id=category_id)
        return queryset



class YachtDetailView(generic.DetailView):
    model = Yacht

    template_name = 'yacht-detail.html'