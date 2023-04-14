from django.test import TestCase
from django.urls import reverse

from catalog.models import *

class YachtListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        Broker.objects.create(broker="Ivakhiv Yacht's Co.")
        broker = Broker.objects.get(id=1)

        category = Category.objects.create(category="Power")

        yacht = Yacht.objects.create(
            price=1000000,
            location='Odesa, Ukraine',
            year=2022,
            make="Ivakhiv Yacht's Co.",
            model='GTX',
            boat_class='Sports Cruiser',
            length=65,
            fuel_type='D',  # Diesel
            hull_material='F',  # Fiberglass
            offered_by=broker,
            description='Description',
            other_details='Other Details',
            # catalog is many-to-many, so it will be assigned be add() later.
        )

        # Create category as a post-step
        category_objects_for_yacht = Category.objects.get(pk=1)
        yacht.category.add(category_objects_for_yacht)
        yacht.save()

    def test_view_url_exists_at_desired_location(self):
        response = self.client.get('/catalog/yachts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop.html')

    def test_get_queryset_function(self):
        response = self.client.get('/catalog/yachts/?category=1')
        self.assertEqual(response.status_code, 200)
        #self.assertTrue('is_paginated' in response.context)
        #self.assertTrue(response.context['is_paginated'] == False)
        self.assertEqual(len(response.context['yacht_list']), 1)