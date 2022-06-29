from django.urls import path
from . import views
urlpatterns = [
 path ('jugadores/', views.list_jugadores, name="Jugadores"),
 path ('jugadores/crear', views.crear_jugador, name="CrearJugador"),
 path('equipos/', views.list_equipos, name="Equipos"),
 path('ligas/', views.list_ligas, name="Ligas"),

] 