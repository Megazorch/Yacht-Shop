from django.contrib import admin
from .models import Broker, Yacht, Specifications, Propulsion

admin.site.register(Broker)
admin.site.register(Yacht)
admin.site.register(Specifications)
admin.site.register(Propulsion)