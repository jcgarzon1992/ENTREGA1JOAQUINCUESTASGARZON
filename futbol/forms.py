from django import forms
from django.core.validators import MinValueValidator, MaxValueValidator

class JugadorFormulario(forms.Form):   
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    peso = forms.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(200)])
    altura = forms.IntegerField(validators=[MinValueValidator(140), MaxValueValidator(210)])
    edad = forms.IntegerField(validators=[MinValueValidator(15), MaxValueValidator(45) ])
    dorsal= forms.IntegerField()
    posicion= forms.CharField(max_length=4)