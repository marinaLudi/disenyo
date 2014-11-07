#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import Pasajero
from db.gestordb import GestorDB

class GestorGestionarPasajeros:
	def buscar(self, nombre, apellido, tipoDocu, Documento):
		database = GestorDB()

		return database.buscarPasajero(nombre, apellido, tipoDocu, Documento)
	
	def crearPasajero(self,DtoPasajero):	
		if self.completo(DtoPasajero):
			print "completo"
			pasajero = Pasajero()
			pasajero.nombre = DtoPasajero.nombre
			pasajero.apellido=DtoPasajero.apellido
			print pasajero.nombre
			

		
	def completo(self,DtoPasajero):
		if DtoPasajero.nombre is "":
			print "nombre es null"
			return False
		if DtoPasajero.apellido is "":
			print "apellido es null"
			return False
		else:
			return True
		

