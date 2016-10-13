from django.contrib import admin

# Register your models here.

from .models import Inmueble
from leaflet.admin import LeafletGeoAdmin


admin.site.register(Inmueble)
