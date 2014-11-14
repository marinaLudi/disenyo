#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import Pasajero, Documento, Iva, Ocupacion
from db.gestordb import GestorDB
#from gestordireccion import GestorDireccion

class GestorGestionarPasajeros:
	def buscar(self, nombre, apellido, tipoDocu, documento):
		gestordb = GestorDB()

		return gestordb.buscarPasajero(nombre, apellido, tipoDocu, documento)
	
	def crearPasajero(self, dtoPasajero):	
		omisiones = self.completo(dtoPasajero)
		if not omisiones:
		
			# Llamamos al gestor de direcciones
			#gestorDireccion = GestorDireccion()
			#direccion_aux = gestorDireccion.crearDireccion(dtoPasajero)

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
			arregloPasajeros = self.buscarPasajero(pasajero.nombre,
					pasajero.apellido, pasajero.tipoDocu, pasajero.documento)
			
			if self.existePasajero(arregloPasajeros):
				return False
			else:
				self.completarCarga(pasajero)
				return True

		else:
			return omisiones
		

	def completo(self, dtoPasajero):
		# Hacemos una lista con las omisiones
		omisiones=list()
		
		for atributo in dtoPasajero.pack:
			if not atributo.startwith("id"):
				for elemento in atributo:
					if elemento is None:
						omisiones.append(elemento)

		return omisiones


	def existePasajero(self, arregloPasajeros):
		# Verificamos si el arreglo esta lleno o vacío
		if arregloPasajeros:

			# Lleno
			return True
		else:

			# Vacio
			return False
	

	def completarCarga(self, pasajero):
		gestordb = GestorDB()
		guardarObjeto(pasajero)
