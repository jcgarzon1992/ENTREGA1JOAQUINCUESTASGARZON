from datetime import date
from django.shortcuts import redirect, render

from futbol.forms import JugadorFormulario
from .models import Jugador, Liga, Equipo

# Listado de jugadores

def list_jugadores(request):
	jugadores = Jugador.objects.all()
	return render(request, "jugadores.html", {"lista_jugadores":jugadores})


# Crear jugador
def crear_jugador(request):
	if request.method == 'POST':

		miFormulario = JugadorFormulario(request.POST) # aquí mellega toda la información del html

		print(miFormulario)

		if miFormulario.is_valid():   #Si pasó la validación de Django

			informacion = miFormulario.cleaned_data

			jugador = Jugador(nombre=informacion['nombre'], apellido=informacion['apellido'], altura= informacion['altura'], peso= informacion['peso'],edad=informacion['edad'], dorsal= informacion['dorsal'],posicion= informacion['posicion'])

			jugador.save()
			return redirect(list_jugadores)			
		else:
			return render(request, "crear_jugador.html", {"miFormulario":miFormulario})

	else: 
		miFormulario= JugadorFormulario() #Formulario vacio para construir el html
	return render(request, "crear_jugador.html", {"miFormulario":miFormulario})




# Equipos
def list_equipos(request):
	Equipo.objects.all().delete()
	equipo1 =Equipo(nombre='PSG',pais='Francia')
	equipo2 =Equipo(nombre='Boca',pais='Argentina' )
	equipo1.save()
	equipo2.save()
	equipos = Equipo.objects.all()
	return render(request, "equipos.html", {"lista_equipos":equipos})

# Ligas
def list_ligas(request):
	Liga.objects.all().delete()
	liga1 =Liga(nombre='Liga1',pais='Francia')
	liga2 =Liga(nombre='Primera División',pais='Argentina' )
	liga1.save()
	liga2.save()
	ligas = Liga.objects.all()
	return render(request, "ligas.html", {"lista_ligas":ligas} )