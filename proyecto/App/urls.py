from django.urls import path
from App import views

urlpatterns= [
    path("", views.inicio, name="Inicio"),
    path("Videos", views.videos, name="Videos"),
    path("Registro", views.registro, name= "Registro"),
    path ("Streamers", views.streamers, name= "Streamers"),
    path('viewerFormulario', views.viewerFormulario, name="viewerFormulario"),
    path('streamerFormulario', views.streamerFormulario, name="streamerFormulario"),
    path('videoFormulario', views.videoFormulario, name="videoFormulario"),
    path('busquedaVideo',views.busquedaVideo,name="BusquedaVideo"),
    path('buscarVideo', views.buscarVideo),
]