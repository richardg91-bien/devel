"""alpha2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin
from inmo.views import buscador, inmuebles_list, signup, inmueble_detail, alta_inmueble, get_ciudades 
from home.views import index
from inmo.models import Inmueble
from django.conf import settings
from django.contrib.auth.views import login, logout


urlpatterns = [
    url(r'^admin/', admin.site.urls),
#   url(r'',include('inmo.urls')),
#   url(r'^$', views.main, name='main'),
    url(r'^$', index, name='main'),                   
    url(r'^inmueble/listado/$', inmuebles_list, name='listado'),
    url(r'^buscador$', buscador, name='buscador'),
    url(r'^signup$', signup, name='signup'),
    url(r'^login$', login, {'template_name': 'inmo/login.html'}, name='login'),
    url(r'^logout$', logout, {'template_name': 'inmo/logout.html'}, name='logout'),
    url(r'^inmueble/(?P<inmueble_id>[0-9]+)/$', inmueble_detail, name='inmueble_detail'),
    url(r'^inmueble/alta/$', alta_inmueble, name='alta_inmueble'),
    url(r'^ciudad/listado/$', get_ciudades, name='ciudad_listado')
]
