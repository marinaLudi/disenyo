#### Gestor Mostrar Ocupar Habitacion ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.gestordb import GestorDB, Singleton
from db.models import Estadia

class GestorOcuparHab:
	def ocuparHab(self,pasajero,tipoPasajero,habitacion,fecha_inicio,fecha_fin):
		if tipoPasajero == 'responsable':
			habitacion = Estadia(fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,nro_habitacion=habitacion.getNumero())
