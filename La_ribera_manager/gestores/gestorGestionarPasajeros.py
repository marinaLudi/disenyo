#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import Pasajero, Documento, Iva, Ocupacion, Pais, Nacionalidad
from db.gestordb import GestorDB, Singleton
from objetos.dtopasajero import dtoPasajero
from gestordireccion import GestorDireccion

class GestorGestionarPasajeros:
	def buscar(self, nombre, apellido, tipoDocu, documento):
		gestordb = GestorDB()

		return gestordb.buscarPasajero(nombre, apellido, tipoDocu, documento)
	
	def crearPasajero(self, dtoPasajero):	

		# Comprobamos si el usuario omitio algun dato
		omisiones = self.completo(dtoPasajero)
		if not omisiones:
			# Creamos el objeto pasajero
			pasajero = construirPasajero(dtoPasajero)
			
			# Corroboramos si hay un pasajero con los mismos datos en la db
			arregloPasajeros = self.buscar(pasajero.nombre,
					pasajero.apellido,
					pasajero.documento.tipo,
					pasajero.documento.codigo)

			if self.existePasajero(arregloPasajeros):
				return False
			else:
				self.completarCarga()
				return True
		
		else:
			return omisiones


	def completo(self, dtoPasajero):
		# Hacemos una lista con las omisiones
		omisiones=list()
		
		for atributo in dtoPasajero.pack():
			if type(atributo) == dict:
				for atrName, value in atributo.iteritems():
					if value is None:
						omisiones.append(atrName)
			else:
				if atributo is None:
					omisiones.append(atributo)

		return omisiones


	def existePasajero(self, arregloPasajeros):
		# Verificamos si el arreglo esta lleno o vacio
		if arregloPasajeros:

			# Lleno
			return True
		else:

			# Vacio
			return False
			

	def completarCarga(self, pasajero):
		gestordb = GestorDB()
		guardarObjeto(pasajero)

	
	def construirPasajero(self, dtoPasajero):

		# Se mapea el dto a un objeto pasajero
		gestorDir = GestorDireccion()
		direccion = gestorDir.crearDireccion(dtoPasajero)
		
		# Obtenemos informacion necesaria de la db
		gestordb = GestorDB()
		ocupacion = gestordb.getObjbyID(Ocupacion, {'id_ocupacion':dtoPasajero.id_ocupacion})
		nacionalidad = gestordb.getObjbyID(Nacionalidad, {'id_nacionalidad':dtoPasajero.id_nacionalidad})
		iva = gestordb.getObjbyID(IVA, {'id_iva':dtoPasajero.id_iva})

		# Creamos objetos pertinentes
		documento = Documento(**dtoPasajero.atributosDocumento)
		pasajero = Pasajero(documento=documento,
				direccion=direccion,
				nacionalidad=nacionalidad,
				ocupacion=ocupacion,
				iva=iva,
				**dtoPasajero.atributosPasajero)

		return pasajero
		
		
		
		
