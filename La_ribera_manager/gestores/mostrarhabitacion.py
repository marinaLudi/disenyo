#!/usr/bin/python
#### Interfaz Mostrar Estado Habitacion ####

import sys, os, inspect

# Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk, Gdk
from db.gestordb import GestorDB, Singleton
from db.models import Habitacion, Estadia,Reserva

# Globals
BORDE_ANCHO = 25
VENTANA_ANCHO = 530
VENTANA_ALTO = 735


class GestorMostrarEstado:
	
	gestor = GestorDB()
	
	def listaHabitaciones(self):
		return self.gestor.getTabla(Habitacion)
	
	def estadoHabitacion(self,habitacion,fecha):
		if self.gestor.getEstado(Estadia,habitacion,fecha):
			return 'red'
		elif self.gestor.getEstado(Reserva,habitacion,fecha):
			return 'yellow'
		else:
			return 'blue'

	
