from django.shortcuts import render, get_object_or_404
from .models import Inmueble
from django.utils import timezone
from .forms import InmuebleForm
from django.shortcuts import redirect
# Create your views here.

def inmuebles_list(request):
	inmuebles = Inmueble.objects.filter()
	return render(request, 'inmo/inmuebles_list.html', {'inmuebles': inmuebles})

def inmueble_detail(request, inmueble_id):
	inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
	return render(request, 'inmo/inmueble_detail.html', {'inmueble': inmueble})

def alta_inmueble(request):
	if request.method == "POST":
            form = InmuebleForm(request.POST)
            if form.is_valid():
                inmueble = form.save(commit=False)
                inmueble.creador = request.user
                inmueble.fecha_publicacion = timezone.now()
                inmueble.save()
                return redirect('inmueble_detail', inmueble_id=inmueble.pk)
	else:
            form = InmuebleForm()
	return render(request, 'inmo/inmueble_edit.html', {'form': form})

