"""
This module contains the tests for views.py.
"""
from django.test import TestCase
from django.urls import reverse

from catalog import models


class YachtListViewTest(TestCase):
    """ Test module for Paginated Yacht List View """

    @classmethod
    def setUpTestData(cls):
        # Set up non-modified objects used by all test methods
        broker = models.Broker.objects.create(broker="Ivakhiv Yacht's.")

        category_objects_for_yacht = models.Category.objects.create(
            category="Sail")

        yacht = models.Yacht.objects.create(
            price=1000000,
            location='Kiev, Ukraine',
            year=2022,
            make="Ivakhiv Yacht's.",
            model='GT',
            boat_class='Sail',
            length=65,
            fuel_type='E',
            hull_material='C',
            offered_by=broker,
            description='Description',
            other_details='Other Details',
            # catalog is many-to-many, so it will be assigned be add() later.
        )

        # Create category as a post-step
        # Category.objects.get(pk=1)
        yacht.category.add(category_objects_for_yacht)
        yacht.save()

    def test_view_url_exists_at_desired_location(self):
        """ Testing if the url exists """
        response = self.client.get('/catalog/yachts/')
        self.assertEqual(response.status_code, 200)

    def test_view_url_accessible_by_name(self):
        """ Testing if the url accessible by name """
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)

    def test_view_uses_correct_template(self):
        """ Testing if the template is used """
        response = self.client.get(reverse('shop'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'shop.html')

    def test_get_queryset_function(self):
        """ Testing if the function is used """
        response = self.client.get('/catalog/yachts/?category=2')   # only Sail
        self.assertEqual(response.status_code, 200)
        # self.assertTrue('is_paginated' in response.context)
        # self.assertTrue(response.context['is_paginated'] == False)
        self.assertEqual(len(response.context['yacht_list']), 1)
