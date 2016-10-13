from django import forms
from .models import Inmueble
from django.contrib.auth.models import User
from django.forms import ModelForm


class InmuebleForm(ModelForm):
    class Meta:
	model = Inmueble
	fields = ('titulo', 'descripcion', 'banos', 'habitaciones', 'location',)

class SignUpForm(ModelForm):
    class Meta:
	model = User
	fields = ['username', 'password', 'email', 'first_name', 'last_name']
	widgets = {'password': forms.PasswordInput(),}



class DireccionForm(forms.Form):
    direccion = forms.CharField()
