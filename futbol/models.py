from sys import maxsize
from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator

# Create your models here.
class Jugador(models.Model):
	nombre = models.CharField(max_length=100)
	apellido = models.CharField(max_length=100)
	peso = models.IntegerField(validators=[MinValueValidator(30), MaxValueValidator(200)])
	altura = models.IntegerField(validators=[MinValueValidator(140), MaxValueValidator(210)])
	edad = models.IntegerField(validators=[MinValueValidator(15), MaxValueValidator(45) ])
	dorsal= models.BigIntegerField()
	posicion= models.CharField(max_length=4)


# Create your models here.

class Liga(models.Model):
	nombre = models.CharField(max_length=50)
	pais = models.CharField(max_length=50)	

# Create your models here.

class Equipo(models.Model):
	nombre = models.CharField(max_length=60)
	pais = models.CharField(max_length=50)		
	

	

