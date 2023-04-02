from django.shortcuts import render
from .models import Broker, Yacht, Specifications, Propulsion
from django.views import generic
from django.db.models import F

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_yachts = Yacht.objects.all().count()
    yachts = Yacht.objects.order_by('-price')[:3]



    context = {
        'num_yachts': num_yachts,
        'yachts': yachts,
        'num_instances': '1',
        'num_instances_available': '1',
        'num_authors': '1',
        'num_genres' : 'num_genres',
        'num_books_special' : 'num_books_special',
        'num_visits': 'num_visits',
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)

"""def shop(request):
    View function for shop page of site.
    context = {

    }
    # Render the HTML template index.html with the data in the context variable
    return render(request, 'shop.html', context=context)"""


class YachtListView(generic.ListView):
    model = Yacht

    template_name = 'shop.html'  # Specify your own template name/location


class YachtDetailView(generic.DetailView):
    model = Yacht

    template_name = 'yacht-detail.html'