from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.validators import MinValueValidator, MaxValueValidator
from django.contrib.auth.models import User

class JugadorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    peso = forms.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(200)])
    altura = forms.IntegerField(validators=[MinValueValidator(140), MaxValueValidator(210)])
    edad = forms.IntegerField(validators=[MinValueValidator(15), MaxValueValidator(45) ])
    dorsal= forms.IntegerField()
    posicion= forms.CharField(max_length=4)
    
class LigaFormulario(forms.Form):
    país = forms.CharField(max_length=50)
    liga = forms.CharField(max_length=50)
    
class EquipoFormulario(forms.Form):
    nombre = forms.CharField(max_length=60)
    país = forms.CharField(max_length=50)

class BuscadorFormulario(forms.Form):
    buscar = forms.CharField(max_length=200)

class UserRegisterForm(UserCreationForm):

    username = forms.CharField()
    email = forms.EmailField()
    password1 = forms.CharField(label='Contraseña', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repetir la contraseña', widget=forms.PasswordInput) 
   
    last_name = forms.CharField()
    first_name = forms.CharField()
    imagen_avatar = forms.ImageField(required=False)    
    
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2', 'last_name', 'first_name'] 
        #Saca los mensajes de ayuda
        help_texts = {k:"" for k in fields}