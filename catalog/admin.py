from django.contrib import admin
from .models import *

admin.site.register(Broker)
admin.site.register(Category)
admin.site.register(Yacht)
admin.site.register(Specifications)
admin.site.register(Propulsion)
admin.site.register(Image)
admin.site.register(Cart)
admin.site.register(CartLineItem)