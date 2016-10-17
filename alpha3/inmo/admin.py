from django.contrib.gis import admin

# Register your models here.

from .models import Inmueble, Barrio, Ciudad, Pais



class LocationAdmin(admin.OSMGeoAdmin):
    default_lon = -7145
    default_lat = -3686
    default_zoom = 5
    # ----- Customized Base Layer -----
    #wms_url = 'http://geodaten.metropoleruhr.de/spw/spw_web'
    #wms_layer = 'spw_web'
    #wms_name = 'Stadtplan'
    #map_template = 'gis/admin/openlayers.html'



    search_fields = ['titulo']
    list_display = ['titulo','location']
    readonly_fields = ['slug']


class BarrioAdmin(admin.OSMGeoAdmin):

    search_fields = ['nombre']
    list_display = ['nombre']



class CiudadAdmin(admin.OSMGeoAdmin):

    search_fields = ['nombre']
    list_display = ['nombre']



class PaisAdmin(admin.OSMGeoAdmin):

    search_fields = ['nombre']
    list_display = ['nombre']




admin.site.register(Inmueble, LocationAdmin)

admin.site.register(Barrio, BarrioAdmin)

admin.site.register(Ciudad, CiudadAdmin)

admin.site.register(Pais, PaisAdmin)
