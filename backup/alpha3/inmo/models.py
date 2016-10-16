from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from geopy import geocoders
from geopy.geocoders import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError
from urllib2 import URLError

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=150)

    def __unicode__(self):
        return self.nombre

class Ciudad(models.Model):
    nombre = models.CharField(max_length=150)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre


class Barrio(models.Model):
    nombre = models.CharField(max_length=150)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)

    def __unicode__(self):
        return self.nombre



class Inmueble(models.Model):
    creador = models.ForeignKey('auth.User')
    titulo = models.CharField(max_length=60, blank=False)
    descripcion = models.CharField(max_length=20, null=True, blank=True)
    banos = models.CharField(max_length=5, null=True, blank=True)
    habitaciones = models.CharField(max_length=5, null=True, blank=True)
    metros_terreno = models.CharField(max_length=5, null=True, blank=True)
    metros_cubiertos = models.CharField(max_length=5, null=True, blank=True)
    email = models.EmailField(null=True, blank=False)
    info = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)
    direccion = models.CharField(max_length=150, blank=False)
    location = gis_models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)    
    gis = gis_models.GeoManager()
    objects = models.Manager()
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)


    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo


    def save(self, **kwargs):
        if not self.location:
            address = u'%s %s' % (self.ciudad.nombre, self.direccion)
            address = address.encode('utf-8')
            geocoder = GoogleV3()
            try:
                _, latlon = geocoder.geocode(address)
            except (URLError, GeocoderQueryError, ValueError):
                pass
            else:
                point = "POINT(%s %s)" % (latlon[1], latlon[0])
                self.location = geos.fromstr(point)
        super(Inmueble, self).save()


class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)


