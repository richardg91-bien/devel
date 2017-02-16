from django.utils import timezone
from django.contrib.gis.db import models
from django.contrib.gis import geos
from geopy import geocoders
from geopy.geocoders import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError
from urllib2 import URLError
from autoslug import AutoSlugField
from django_extensions.db import fields as ext_fields

# Create your models here.

class Pais(models.Model):
    nombre = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='nombre', max_length=255)
    uuid = ext_fields.UUIDField(auto=True)
    area = models.PolygonField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Paises"

class Ciudad(models.Model):
    nombre = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='nombre', max_length=255)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    uuid = ext_fields.UUIDField(auto=True)
    area = models.PolygonField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Ciudades"

class Barrio(models.Model):
    nombre = models.CharField(max_length=150)
    slug = AutoSlugField(populate_from='nombre', max_length=255)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    uuid = ext_fields.UUIDField(auto=True)
    area = models.PolygonField(null=True, blank=True)
    objects = models.GeoManager()

    def __unicode__(self):
        return self.nombre

    class Meta:
        verbose_name_plural = "Barrios"


class Inmueble(models.Model):
    creador = models.ForeignKey('auth.User')

    email = models.EmailField(null=True, blank=False)
    info = models.TextField(null=True, blank=True)
    fecha_creacion = models.DateTimeField(auto_now_add=True)
    fecha_publicacion = models.DateTimeField(blank=True, null=True)

    titulo = models.CharField(max_length=60, blank=False)
    descripcion = models.CharField(max_length=20, null=True, blank=True)

    direccion = models.CharField(max_length=150, blank=False)
    calle = models.CharField(max_length=150, blank=False)
    altura = models.CharField(max_length=6, blank=False)
    pais = models.ForeignKey(Pais, on_delete=models.CASCADE)
    ciudad = models.ForeignKey(Ciudad, on_delete=models.CASCADE)
    barrio = models.ForeignKey(Barrio, on_delete=models.CASCADE)

    metros_terreno = models.CharField(max_length=5, null=True, blank=True)
    metros_cubiertos = models.CharField(max_length=5, null=True, blank=True)
    antiguedad = models.CharField(max_length=2, blank=False)

    banos = models.CharField(max_length=5, null=True, blank=True)
    habitaciones = models.CharField(max_length=5, null=True, blank=True)
    ambientes = models.CharField(max_length=2, blank=False)
    plantas = models.CharField(max_length=2, blank=False)
    pileta = models.CharField(max_length=2, blank=False)
    cochera = models.CharField(max_length=2, blank=False)
    patio = models.CharField(max_length=2, blank=False)

    precio = models.CharField(max_length=10, blank=False)
    location = models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)    
    gis = models.GeoManager()
    objects = models.Manager()
    slug = AutoSlugField(populate_from='titulo', max_length=255)
    uuid = ext_fields.UUIDField(auto=True)

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

    class Meta:
        verbose_name_plural = "Inmuebles"

class Cliente(models.Model):
    nombre = models.CharField(max_length=150)
    telefono = models.CharField(max_length=150)
    email = models.CharField(max_length=150)
    direccion = models.CharField(max_length=150)

    class Meta:
        verbose_name_plural = "Clientes"

class Mensaje(models.Model):
    fecha_envio = models.DateTimeField(auto_now_add=True)
    fecha_respuesta = models.DateTimeField(blank=True, null=True)
    respondio = models.ForeignKey('auth.User')
    titulo = models.TextField(null=True, blank=True)
    cuerpo = models.TextField(null=True, blank=True)
    inmueble = models.ForeignKey(Inmueble)
    

    class Meta:
        verbose_name_plural = "Mensajes"
