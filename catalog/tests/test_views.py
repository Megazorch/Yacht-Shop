from django.test import TestCase
from django.urls import reverse

from catalog.models import *

class YachtListViewTest(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass


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