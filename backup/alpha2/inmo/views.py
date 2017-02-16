from django.shortcuts import render, get_object_or_404
from .models import Inmueble
from django.utils import timezone
from .forms import *
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.template.context import RequestContext
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

# Create your views here.

def main(request):
        context=RequestContext(request)
	return render(request, 'inmo/main.html', {})


def inmuebles_list(request):
	inmuebles = Inmueble.objects.filter()
	return render(request, 'inmo/inmuebles_list.html', {'inmuebles': inmuebles})

def inmueble_detail(request, inmueble_id):
	inmueble = get_object_or_404(Inmueble, pk=inmueble_id)
	return render(request, 'inmo/inmueble_detail.html', {'inmueble': inmueble})

@login_required
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
 
    data = {
        'form': form,
    }
    return render(request,'inmo/signup.html', data, RequestContext(request))

