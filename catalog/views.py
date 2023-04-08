from django.db.models import Q
from django.shortcuts import render
from .models import *
from django.views import generic


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


class YachtListView(generic.ListView):
    model = Yacht
    template_name = 'shop.html'  # Specify your own template name/location
    
    def get_context_data(self, **kwargs):
        # Get all Yachts with category="Power"
        power_yachts = Yacht.objects.filter(category__category="Power").exclude(Q(category__category="Sail"))
        # Get unique boat_class values
        power_classes = power_yachts.values_list('boat_class', flat=True).distinct()

        # Get all Yachts with category="Sail"
        sail_yachts = Yacht.objects.filter(category__category="Sail").exclude(Q(category__category="Power"))
        # Get unique boat_class values
        sail_classes = sail_yachts.values_list('boat_class', flat=True).distinct()

        # Get all Yachts with category="Power, Sail"
        #both_category_yachts = Yacht.objects.filter(Q(category__category="Power")
                                                    #| Q(category__category="Sail")).distinct()
        both_category_yachts = Yacht.objects.filter(category__category="Sail")

        # Get unique boat_class values
        both_classes = both_category_yachts.values_list('boat_class', flat=True).distinct()

        context = super().get_context_data(**kwargs)
        # The set() function is used to convert the list to a set,
        # which automatically removes duplicates
        context['power_yachts'] = list(set(power_classes))
        context['sail_yachts'] = list(set(sail_classes))
        context['both_category_yachts'] = list(set(both_classes))
        return context



class YachtDetailView(generic.DetailView):
    model = Yacht

    template_name = 'yacht-detail.html'