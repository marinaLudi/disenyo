#### Gestor Mostrar Estado Habitacion ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.gestordb import GestorDB, Singleton

class GestorMostrarEstadoHab:
	def selectHab(self, fechaIni, fechaFin):
		gestordb = GestorDB()

		arregloHabitaciones = gestordb.getHab()

		print arregloHabitaciones
