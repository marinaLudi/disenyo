#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from objetos.pasajero import pasajero
from db.gestordb import GestorDB

class GestorGestionarPasajeros:
	def buscar(self, nombre, apellido, tipoDocu, Documento):
		database = GestorDB()

		return database.buscarPasajero(nombre, apellido, tipoDocu, Documento)
	
	def crearPasajero(self,DtoPasajero):
		try:
			self.completo(DtoPasajero)
		except:
			print 'eh?'

		
	def completo(self,DtoPasajero):
		print DtoPasajero.nombre
		

