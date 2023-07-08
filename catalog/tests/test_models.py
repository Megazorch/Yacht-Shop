"""
Test module for models.
"""
from django.test import TestCase

from catalog import models

class YachtModelTest(TestCase):
    """ Test module for Yacht model """
    @classmethod
    def setUpTestData(cls):
        """Set up non-modified objects used by all test methods """
        broker = models.Broker.objects.create(broker="Ivakhiv Yacht's Co.")

        models.Category.objects.create(category="Power")

        models.Yacht.objects.create(
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
            # catalog is many-to-many, so it will be assigned by add() later.
        )

        # yacht.category.add(category)

    def test_year_label(self):
        """ Testing year label """
        yacht = models.Yacht.objects.get(id=1)
        field_label = yacht._meta.get_field('year').verbose_name
        self.assertEqual(field_label, 'year')

    def test_make_max_length(self):
        """ Testing make max length """
        yacht = models.Yacht.objects.get(id=1)
        max_length = yacht._meta.get_field('make').max_length
        self.assertEqual(max_length, 40)

    def test_object_name_is_year_make_model_length(self):
        """ Testing object name is year make model length """
        yacht = models.Yacht.objects.get(id=1)
        expected_object_name = f'{yacht.year} {yacht.make} {yacht.model} | {yacht.length} ft.'
        self.assertEqual(str(yacht), expected_object_name)


    def test_catalog_proper_assign(self):
        """ Testing catalog proper assign """
        yacht = models.Yacht.objects.get(id=1)
        category = models.Category.objects.get(pk=1)  # ChatGPT
        yacht.category.add(category)  # ChatGPT

        # Retrieve the category value for the yacht
        categories = yacht.category.all()   # categories got list of numbers
        category_values = [c.category for c in categories]

        # Assert that the category value is 'Power'
        self.assertIn('Power', category_values)

    def test_full_fuel_type_name(self):
        """ Testing full fuel type name """
        yacht = models.Yacht.objects.get(id=1)
        full_fuel_type = yacht.get_fuel_type_display()

        self.assertEqual('Diesel', full_fuel_type)


    def test_custom_all_basic_fields_function(self):
        """ Testing custom all basic fields function """
        yacht = models.Yacht.objects.get(id=1)
        list_of_field_names = yacht.all_basic_fields()

        self.assertIsInstance(list_of_field_names, list)
        self.assertEqual(len(list_of_field_names), 10)
        self.assertEqual(list_of_field_names[0], ('Year', 2022))
        self.assertEqual(list_of_field_names[5], ('Fuel type', 'Diesel'))


    def test_get_absolute_url(self):
        """ Testing get absolute url"""
        yacht = models.Yacht.objects.get(id=1)
        # This will also fail if the urlconf is not defined.
        self.assertEqual(yacht.get_absolute_url(), '/catalog/yachts/1')
