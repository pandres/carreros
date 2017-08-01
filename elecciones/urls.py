# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views


urlpatterns = [
    url('^escuelas.geojson$', views.LugaresVotacionGeoJSON.as_view(), name='geojson'),
    url('^escuelas/(?P<pk>\d+)$', views.EscuelaDetailView.as_view(), name='detalle_escuela'),
    url('^mapa$', views.Mapa.as_view(), name='mapa'),
    url('^mapa1$', views.Mapa1.as_view(), name='mapa1')

]
