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


	def asignarPasajero(self,tipoPasajero, id_pasajero, fecha_ini, fecha_fin):
		if tipoPasajero == 'responsable':
		    if self.responsable is None:
		        self.responsable = self.gestordb.getObjetoID(Pasajero,id_pasajero)
		    else:
		         return False
		elif tipoPasajero == 'acompanyante':
		    verif = self.verificarAcompanyante(id_pasajero,fecha_ini,fecha_fin)
		    if not verif:
		        self.ocupantes.append(self.gestordb.getObjetoID(Pasajero,id_pasajero))
		    else:
		        return verif
		return True


	def ocuparHab(self,habitacion,fecha_inicio,fecha_fin):
		if self.responsable is not None:
			estadia = Estadia(fecha_inicio=fecha_inicio,fecha_fin=fecha_fin,nro_habitacion=habitacion.getNumero(),responsable=self.responsable)
			if self.ocupantes:
				for ocupante in self.ocupantes:
					estadia.ocupantes.append(ocupante)
			habitacion.estadias.append(estadia)
			self.gestordb.guardarObjeto(habitacion)
	
	def verificarAcompanyante (self, id_pasajero, fecha_ini, fecha_fin):
	    hospedado = self.gestordb.buscarHospedado(id_pasajero,fecha_ini, fecha_fin)
	    return hospedado
