from django.db import models
from djmoney.models.fields import MoneyField
from django.urls import reverse  # Used to generate URLs by reversing the URL patterns


class Broker(models.Model):
    """Model representing the maker of yachts."""
    broker = models.CharField(max_length=50, help_text='Enter the name of seller (broker).')

    def __str__(self):
        """String for representing the Model object."""
        return self.broker


class Yacht(models.Model):
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
    price = MoneyField(max_digits=7, decimal_places=0, default_currency='USD', help_text="Enter price of the yacht.")
    location = models.CharField(max_length=35, help_text="Enter the city and country where the yacht is situated.")
    year = models.PositiveIntegerField(help_text="Enter the year of build of the yacht.")
    make = make = models.CharField(max_length=40, help_text="Enter the maker company name.")
    model = models.CharField(max_length=10, help_text="Enter the model type of the yacht.")
    boat_class = models.CharField(max_length=25, help_text="Enter the class of the yacht.")
    length = models.DecimalField(max_digits=4, decimal_places=2, help_text="Enter the exact length of the yacht in ft.")
    # приблизний результат, розділити значення довжина на 3,2808399
    fuel_type = models.CharField(max_length=2, choices=FUEL_TYPES, default='O')
    hull_material = models.CharField(max_length=2, choices=HULL_MATERIAL, default='O')
    hull_shape = models.CharField(max_length=20, blank=True, help_text="Enter hull shape if relevant.")
    hull_warranty = models.PositiveIntegerField(null=True, blank=True)
    offered_by = models.ForeignKey(Broker, on_delete=models.CASCADE, help_text='Enter the name of seller (broker).')
    description = models.TextField(max_length=1000, help_text='Enter a brief description of the yacht')
    contact_info = models.TextField(max_length=100, null=True, blank=True)
    other_details = models.TextField(max_length=1500)

    class Meta:
        ordering = ['make', 'model']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('yacht-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.year} {self.make} {self.model} | {self.length}'


class Propulsion(models.Model):
    """Model representing different types of propulsion of the yachts."""
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE)
    engine_make = models.CharField(max_length=20, help_text="Enter engine maker.")
    engine_model = models.CharField(max_length=20, help_text="Enter engine model.")
    engine_year = models.PositiveIntegerField(help_text="Enter the year of build of the engine.")
    total_power = models.PositiveIntegerField(
                                              help_text="Enter the total power of engine in Horse Powers.")
    engine_hours = models.PositiveIntegerField(null=True, blank=True,
                                               help_text="Enter amount of hours engine has been in use.")
    engine_type = models.CharField(max_length=10, null=True, blank=True)
    drive_type = models.CharField(max_length=25, null=True, blank=True)
    # fuel_type = Yacht.fuel_type
    propeller_type = models.CharField(max_length=15, null=True, blank=True)
    propeller_material = models.CharField(max_length=15, null=True, blank=True)
    folding_propeller = models.BooleanField(null=True, blank=True)

    class Meta:
        ordering = ['engine_make', 'engine_model']

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('engine-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.engine_make} {self.engine_model}'


class Specifications(models.Model):
    """Model representing specific information about yacht."""
    yacht = models.ForeignKey(Yacht, on_delete=models.CASCADE)
    cruising_speed = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True,
                                         help_text="Cruising speed in kn.")
    max_speed = models.DecimalField(max_digits=2, decimal_places=1, null=True, blank=True,
                                    help_text="Maximum speed in kn.")
    length_overall = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, help_text='LOA in ft.')
    max_draft = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, help_text='Max draft in ft.')
    beam = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True, help_text='Beam length in ft.')
    length_at_waterline = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True,
                                              help_text='Length in ft.')
    dry_weight = models.DecimalField(max_digits=4, decimal_places=2, null=True, blank=True,
                                     help_text='Example: 68,343Lb')
    windlass = models.CharField(max_length=25, null=True, blank=True, help_text="Enter type of windlass.")
    fresh_water_tank = models.CharField(max_length=25, null=True, blank=True, help_text="Example: 1 X 87 Gal (Plastic)")
    fuel_tank = models.CharField(max_length=25, null=True, blank=True, help_text="Example: 1 X 87 Gal (Plastic)")
    holding_tank = models.CharField(max_length=25, null=True, blank=True, help_text="Example: 1 X 87 Gal (Plastic)")
    single_berths = models.PositiveIntegerField(null=True, blank=True)
    double_berths = models.PositiveIntegerField(null=True, blank=True)
    cabins = models.PositiveIntegerField(null=True, blank=True)
    heads = models.PositiveIntegerField(null=True, blank=True)

    def get_absolute_url(self):
        """Returns the URL to access a particular author instance."""
        return reverse('specifications-detail', args=[str(self.id)])

    def __str__(self):
        """String for representing the Model object."""
        return f'{self.yacht} - Specifications'



