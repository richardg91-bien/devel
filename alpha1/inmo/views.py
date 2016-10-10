from django.shortcuts import render
from .models import Inmueble
from django.utils import timezone
# Create your views here.

def inmuebles_list(request):
	inmuebles = Inmueble.objects.filter()
        return render(request, 'inmo/inmuebles_list.html', {'inmuebles': inmuebles})