from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^$', views.inmuebles_list, name='home'),
    url(r'^inmueble/(?P<inmueble_id>[0-9]+)/$', views.inmueble_detail, name='inmueble_detail'),
    url(r'^inmueble/alta/$', views.alta_inmueble, name='alta_inmueble'),

    ]