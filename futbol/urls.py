from django.urls import path
from . import views
from django.contrib.auth.views import LogoutView

urlpatterns = [
 path ('jugadores/', views.list_jugadores, name="Jugadores"),
 path ('jugadores/crear', views.crear_jugador, name="CrearJugador"),
 path('equipos/', views.list_equipos, name="Equipos"),
 path('ligas/', views.list_ligas, name="Ligas"),
 path('crear_liga/', views.crear_liga, name="CrearLiga"),
 path('about/', views.about, name="About"),
 path('crear_equipo/', views.crear_equipo, name="CrearEquipo"),
 
 path('login', views.login_request, name="Login"),
 path('register', views.register, name = 'Register'),
 path('logout', views.logout_request, name = 'Logout'),
 
] 