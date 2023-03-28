from django.shortcuts import render
from .models import Broker, Yacht, Specifications, Propulsion
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views import generic

def index(request):
    """View function for home page of site."""

    # Generate counts of some of the main objects
    num_yachts = Yacht.objects.all().count()

    context = {
        'num_yachts': num_yachts,
        'num_instances': '1',
        'num_instances_available': '1',
        'num_authors': '1',
        'num_genres' : 'num_genres',
        'num_books_special' : 'num_books_special',
        'num_visits': 'num_visits',
    }

    # Render the HTML template index.html with the data in the context variable
    return render(request, 'index.html', context=context)
