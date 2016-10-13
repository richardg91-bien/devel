from django.db import models
from django.utils import timezone
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos

# Create your models here.
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
    ciudad = models.CharField(max_length=150, blank=False)
    location = gis_models.PointField(u"longitude/latitude", geography=True, blank=True, null=True)    
    gis = gis_models.GeoManager()
    objects = models.Manager()


    def publish(self):
        self.fecha_publicacion = timezone.now()
        self.save()

    def __str__(self):
        return self.titulo

