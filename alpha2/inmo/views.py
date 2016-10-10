from django.shortcuts import render, get_object_or_404
from .models import Inmueble
from django.utils import timezone
# Create your views here.

def inmuebles_list(request):
	inmuebles = Inmueble.objects.filter()
	return render(request, 'inmo/inmuebles_list.html', {'inmuebles': inmuebles})

def inmueble_detail(request, inmueble_id):
	inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
	return render(request, 'inmo/inmueble_detail.html', {'inmueble': inmueble})

