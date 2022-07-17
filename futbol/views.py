from datetime import date
from django.shortcuts import redirect, render
from django.db.models import Q

from futbol.forms import EquipoFormulario, JugadorFormulario, LigaFormulario, UserRegisterForm
from .models import Jugador, Liga, Equipo
#Decorador por defecto
from django.contrib.auth.decorators import login_required
#Para el login

from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate


# Listado de jugadores
@login_required(login_url='Login')
def list_jugadores(request):
	# jugadores = Jugador.objects.all()
    
	busqueda = request.GET.get('buscar')

	if busqueda:
		jugadores = Jugador.objects.filter(Q(nombre__icontains=busqueda) | Q(apellido__icontains=busqueda))
	else:
		jugadores = Jugador.objects.all()
	return render(request, "jugadores.html", {"lista_jugadores":jugadores})


# Crear jugador
@login_required(login_url='Login')
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
@login_required(login_url='Login')
def list_equipos(request):
	# Equipo.objects.all().delete()
	# equipo1 =Equipo(nombre='PSG',pais='Francia')
	# equipo2 =Equipo(nombre='Boca',pais='Argentina' )
	# equipo3 =Equipo(nombre='Union',pais='Argentina' )
	# equipo1.save()
	# equipo2.save()
	# equipo3.save()
	equipos = Equipo.objects.all()
	return render(request, "equipos.html", {"lista_equipos":equipos})

@login_required(login_url='Login')
def crear_equipo(request):
	if request.method == 'POST':

		miFormulario = EquipoFormulario(request.POST) # aquí mellega toda la información del html

		print(miFormulario)

		if miFormulario.is_valid():   #Si pasó la validación de Django

			informacion = miFormulario.cleaned_data
			equipo = Equipo(nombre=informacion['equipo'], pais=informacion['país'])

			equipo.save()
			return redirect(list_equipos)
			
		else:
			return render(request, "crear_liga.html", {"miFormulario":miFormulario})

	else: 
		miFormulario= EquipoFormulario() #Formulario vacio para construir el html
	return render(request, "crear_equipo.html", {"miFormulario":miFormulario})


# Ligas
@login_required(login_url='Login')
def list_ligas(request):
	ligas = Liga.objects.all()
	# liga1 =Liga(nombre='Liga1',pais='Francia')
	# liga2 =Liga(nombre='Primera División',pais='Argentina' )
	# liga1.save()
	# liga2.save()
	# ligas = Liga.objects.all()
	return render(request, "ligas.html", {"lista_ligas":ligas} )

# Crear Liga
@login_required(login_url='Login')
def crear_liga(request):
	if request.method == 'POST':

		miFormulario = LigaFormulario(request.POST) # aquí me llega toda la información del html

		print(miFormulario)

		if miFormulario.is_valid():   #Si pasó la validación de Django

			informacion = miFormulario.cleaned_data
			liga = Liga(nombre=informacion['liga'], pais=informacion['país'])

			liga.save()
			return redirect(list_ligas)
			
		else:
			return render(request, "crear_liga.html", {"miFormulario":miFormulario})

	else: 
		miFormulario= LigaFormulario() #Formulario vacio para construir el html
	return render(request, "crear_liga.html", {"miFormulario":miFormulario})


def about(request):	
	return render(request, "about.html")

#def home(request):
#	form = AuthenticationForm()
#	return render(request,"home.html", {'form':form} )

def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data = request.POST)
		if form.is_valid():
			usuario = form.cleaned_data.get('username')
			contra = form.cleaned_data.get('password')
			user = authenticate(username=usuario, password=contra)
			if user is not None:
				login(request, user)
				return redirect('Jugadores')
			else:
				return render(request,"home.html", {"mensaje":"Error, datos incorrectos"} )
		else:
			return render(request,"home.html" ,  {"mensaje":"Error, formulario erroneo"})

	form = AuthenticationForm()
	return render(request,"home.html", {'form':form} )




def logout_request(request):
	logout(request) 
	return redirect('Login')

def register(request):
	if request.method == 'POST':
		#form = UserCreationForm(request.POST)
		form = UserRegisterForm(request.POST)
		if form.is_valid():
			username = form.cleaned_data['username']
			form.save()
			return render(request,"home.html" ,  {"mensaje":"Usuario Creado :)"})
	else:
		#form = UserCreationForm()       
		form = UserRegisterForm()     
	return render(request,"registro.html" ,  {"form":form})
