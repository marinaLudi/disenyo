#### Gestor Mostrar Ocupar Habitacion ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.gestordb import GestorDB, Singleton
from db.models import Estadia,Pasajero

class GestorOcuparHab:
	def __init__(self):
		self.responsable = None
		self.ocupantes = []
		self.gestordb = GestorDB()
		
	def asignarPasajero(self,tipoPasajero,id_pasajero):
		if tipoPasajero == 'responsable':
			self.responsable = self.gestordb.getObjetoID(Pasajero,id_pasajero)
		elif tipoPasajero == 'acompanyante':
			self.ocupantes.append(self.gestordb.getObjetoID(Pasajero,id_pasajero))
			
	def ocuparHab(self,habitacion,fecha_inicio,fecha_fin):
		if self.responsable is not None:			
			estadia = Estadia(fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,nro_habitacion=habitacion.getNumero(),responsable=self.responsable)
			if self.ocupantes:
				for ocupante in self.ocupantes:
					estadia.ocupantes.append(ocupante)	
								
			habitacion.estadias.append(estadia)
			self.gestordb.guardarObjeto(habitacion)
		

		

			
