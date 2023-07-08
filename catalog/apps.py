"""
This module is used to configure the catalog app
"""
from django.apps import AppConfig


class CatalogConfig(AppConfig):
    """ CatalogConfig class used to configure the catalog app """
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'catalog'
