from django import forms
import models
from .models import *
from django.contrib.auth.models import User
from django.forms import ModelForm
from urllib2 import URLError

class InmuebleForm(ModelForm):
        
    class Meta:

	model = Inmueble
#	pais = forms.ModelChoiceField(queryset=models.Pais.objects.all())
#        ciudad = forms.ModelChoiceField(queryset=models.Ciudad.objects.none()) # Need to populate this using jquery
#        barrio = forms.ModelChoiceField(queryset=models.Barrio.objects.none()) # Need to populate this using jquery

	fields = ['titulo', 'descripcion', 'banos', 'habitaciones', 'direccion', 'pais', 'ciudad', 'barrio']


class SignUpForm(ModelForm):
    class Meta:
	model = User
	fields = ['username', 'password', 'email', 'first_name', 'last_name']
	widgets = {'password': forms.PasswordInput(),}


class DireccionForm(forms.Form):
    direccion = forms.CharField()
