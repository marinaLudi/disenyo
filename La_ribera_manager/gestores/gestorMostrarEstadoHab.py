#### Gestor Mostrar Estado Habitacion ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.gestordb import GestorDB, Singleton
from gestores.date_operations import daterange, is_in_between
import datetime

class GestorMostrarEstadoHab:
	def selectHab(self, fechaIni, fechaFin):
		# Obtenemos habitaciones
		gestordb = GestorDB()
		arregloHabitaciones = gestordb.getHab()

		tuplas = []
		for habitacion in arregloHabitaciones:
			# Obtenemos estados de la habitacion
			estados = []
			for dia in daterange(fechaIni, fechaFin):
				estados.append(self.obtenerEstado(habitacion, dia))

			# Elegimos color
			color = self.obtenerColores(estados)	

			# Concatenamos resultado
			tuplas.append((habitacion.getNumero(),
				habitacion.getTipo(),
				estados,
				color))


		return tuplas 


	def obtenerEstado(self, habitacion, fecha):
		if self.checkEstado(habitacion.getEstadias(), fecha):
			return 'ocupado'

		else:
			if self.checkEstado(habitacion.getReservas(), fecha):
				return 'reservado'
			
			else:
				if self.checkEstado(habitacion.getMantenimientos(), fecha):
					return 'ocupado'

				else:
					return 'libre'


	def checkEstado(self, restricciones, fecha):
		for restriccion in restricciones:
			if is_in_between(fecha,
					restriccion.getFechaIni(),
					restriccion.getFechaFin()):
				
				return True	

		return False


	def obtenerColores(self, estados):
		colores = []

		for estado in estados:
			if estado is 'ocupado':
				colores.append('red')

			elif estado is 'reservado':
				colores.append('yellow')

			elif estado is 'libre':
				colores.append('blue')


		return colores

