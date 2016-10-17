from django.shortcuts import render, get_object_or_404
from .models import *
from django.utils import timezone
import simplejson
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.shortcuts import render_to_response
from django.core.urlresolvers import reverse
from urllib2 import URLError
from django.contrib.gis import measure
from django.contrib.gis.db import models as gis_models
from django.contrib.gis import geos
from django.db import models
from geopy import geocoders
from geopy.geocoders import GoogleV3
from geopy.geocoders.googlev3 import GeocoderQueryError

# Create your views here.

def main(request):
        context=RequestContext(request)
	return render(request, 'inmo/index.html', {})


def inmuebles_list(request):
	inmuebles = Inmueble.objects.filter()
	return render(request, 'inmo/inmuebles_list.html', {'inmuebles': inmuebles})

def inmueble_detail(request, inmueble_id):
	inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
	return render(request, 'inmo/inmueble_detail.html', {'inmueble': inmueble})


@login_required
def alta_inmueble(request):
            
	form = InmuebleForm(request.POST or None)

	if request.method == "POST":
            if form.is_valid():
                inmueble = form.save(commit=False)
                inmueble.creador = request.user
                inmueble.fecha_publicacion = timezone.now()
                inmueble.save()
                return redirect('inmueble_detail', inmueble_id=inmueble.pk)
	    else:
		form = InmuebleForm()
	return render(request, 'inmo/inmueble_edit.html', {'form': form})


def signup(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():

            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            email = form.cleaned_data["email"]
            first_name = form.cleaned_data["first_name"]
            last_name = form.cleaned_data["last_name"]
 
            user = User.objects.create_user(username, email, password)
            user.first_name = first_name
            user.last_name = last_name
 
            user.save()
 
            return HttpResponseRedirect(reverse('main'))
    else:
        form = SignUpForm()
 
    data = { 'form': form, }
    return render(request,'inmo/signup.html', data)


def geocode_address(direccion):
    direccion = direccion.encode('utf-8')
    geocoder = GoogleV3()
    try:
	_,latlon = geocoder.geocode(direccion)
    except (URLError, GeocoderQueryError, ValueError):
	return none
    else:
	return latlon

def get_inmuebles(longitude, latitude):
    current_point = geos.fromstr("POINT(%s %s)" % (longitude, latitude))
    distance_from_point = {'km': 2}
    inmuebles = Inmueble.gis.filter(location__distance_lte=(current_point, measure.D(**distance_from_point)))
    inmuebles = inmuebles.distance(current_point).order_by('distance')
    return inmuebles.distance(current_point)

#@login_required
def buscador(request):
    context=RequestContext(request)
    form = DireccionForm()
    inmuebles = []
    latitude = ""
    longitude = ""
    if request.POST:
        form = DireccionForm(request.POST)
        if form.is_valid():
            direccion = u'%s %s' % (form.cleaned_data['direccion'], form.cleaned_data['ciudad'])
	    location = geocode_address(direccion)
            if location:
                latitude, longitude = location
                inmuebles = get_inmuebles(longitude, latitude)

    return render(request, 'inmo/buscador.html', {'form': form, 'inmuebles': inmuebles, 'latitude': latitude, 'longitude': longitude})


def get_ciudades(request, pais_id):
    pais = models.Pais.objects.get(pk=pais_id)
    ciudades = models.Ciudad.objects.filter(pais=pais)
    ciudad_dict = {}
    for ciudad in ciudades:
        ciudad_dict[ciudad.id] = ciudad.name
    return HttpResponse(simplejson.dumps(ciudad_dict), mimetype="application/json")

