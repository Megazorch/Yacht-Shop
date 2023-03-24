from django.db import models
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Make(models.Model):
    """Model representing the maker of yachts."""
    make = models.CharField(max_length=40, help_text="Enter the maker company name.")

    def __str__(self):
        """String for representing the Model object."""
        return self.make


class Basics(models.Model):
    """Model representing the basic characteristics of the yacht."""
    FUEL_TYPES = (
        ('D', 'Diesel'),
        ('E', 'Electric'),
        ('GP', 'Gas/Petrol'),
        ('L', 'LPG'),
        ('O', 'Other'),
    )

    HULL_MATERIAL = (
        ('A', 'Aluminum'),
        ('C', 'Composite'),
        ('FC', 'Ferro-Cement'),
        ('F', 'Fiberglass'),
        ('H', 'Hypalon'),
        ('O', 'Other'),
        ('P', 'PVC'),
        ('S', 'Steel'),
        ('W', 'Wood'),
    )

    year = models.IntegerField(max_length=4, help_text="Enter the year of build of the yacht.")
    make = models.ForeignKey(Make, on_delete=models.CASCADE, null=True)
    model = models.CharField(max_length=10, help_text="Enter the model type of the yacht.")
    boat_class = models.CharField(max_length=25, help_text="Enter the class of the yacht.")
    length = models.FloatField(help_text="Enter the exact length of the yacht.")
    fuel_type = models.CharField(max_length=2, choices=FUEL_TYPES, default='O')
    hull_material = models.CharField(max_length=2, choices=HULL_MATERIAL, default='O')
    hull_shape = models.CharField(max_length=20, blank=True, help_text="Enter hull shape if relevant.")
    hull_warranty = models.IntegerField(max_length=2, null=True, blank=True)
    offered_by = models.CharField(max_length=50, help_text='Enter the name of seller.')
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the yacht')

    class Meta:
        ordering = ['make', 'model']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('yacht-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.year} {self.make} {self.model} | {self.length}'
