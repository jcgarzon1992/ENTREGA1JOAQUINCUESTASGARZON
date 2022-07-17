from django.contrib import admin

from futbol.models import Equipo, Jugador, Liga

# Register your models here.

admin.site.register(Liga)
admin.site.register(Jugador)
admin.site.register(Equipo)