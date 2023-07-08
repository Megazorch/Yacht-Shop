"""
Admin panel for yacht_site
"""
from django.contrib import admin
from catalog import models

admin.site.register(models.Broker)
admin.site.register(models.Category)
admin.site.register(models.Yacht)
admin.site.register(models.Specifications)
admin.site.register(models.Propulsion)
admin.site.register(models.Image)
admin.site.register(models.Cart)
admin.site.register(models.CartLineItem)
