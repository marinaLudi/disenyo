#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import Pasajero, Documento, Iva, Ocupacion
from db.gestordb import GestorDB
from gestordireccion import GestorDireccion

class GestorGestionarPasajeros:
	def buscar(self, nombre, apellido, tipoDocu, Documento):
		gestordb = GestorDB()

		return gestordb.buscarPasajero(nombre, apellido, tipoDocu, Documento)
	
	def crearPasajero(self, dtoPasajero):	
		if self.completo(dtoPasajero):
		
			# Llamamos al gestor de direcciones
			gestorDireccion = GestorDireccion()
			direccion_aux = gestorDireccion.crearDireccion(dtoPasajero)

			# Creamos lista con objetos a mapear
			objetos_aux = [Documento(dtoPasajero.atributosDocumento),
					Ocupacion(dtoPasajero.atributosOcupacion),
					Iva(dtoPasajero.atributosIva)]

			# Concatenamos direccion
			objetos_aux.extend(direccion_aux)

			# Instanciamos pasajero y lo agregamos a la lista de objetos
			pasajero = Pasajero(dtoPasajero.atributosPasajero)
			objetos_aux.append(pasajero)
				
			# Llamamos al gestor de base de datos y obtenemos una lista de pasajeros
			gestordb = GestorDB()
			arregloPasajeros = self.obtenerPasajero(pasajero) 
			
			if existePasajero(arregloPasajeros):
				return False
			else:
				completarCarga(pasajero)
				return True
		else:
			return faltantes(dtoPasajero)

			
		
	def completo(self, dtoPasajero):
		omisiones=list()
		
