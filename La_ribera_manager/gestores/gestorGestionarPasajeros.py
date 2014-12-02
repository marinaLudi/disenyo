#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import Pasajero, Documento, Iva, Ocupacion, Pais, Nacionalidad, TipoDocumento
from db.gestordb import GestorDB, Singleton
from objetos.dtopasajero import DtoPasajero
from gestordireccion import GestorDireccion

class GestorGestionarPasajeros:
	def buscar(self, nombre, apellido, tipoDocu, documento):
		gestordb = GestorDB()

		arregloPasajeros = gestordb.buscarPasajero(nombre, apellido, tipoDocu, documento)
		
		# Comprobamos si la lista tiene algun pasajero 
		# En caso de que contenga al menos un pasajero se devuelve la lista
		# Si la lista esta vacia se devuelve False
		if self.existePasajero(arregloPasajeros):
			return arregloPasajeros
		else:
			return False

	
	def crearPasajero(self, dtoPasajero):	

		# Comprobamos si el usuario omitio algun dato
		omisiones = self.completo(dtoPasajero)
		if not omisiones:
			# Creamos el objeto pasajero
			pasajero = self.construirPasajero(dtoPasajero)
			
			# Corroboramos si hay un pasajero con los mismos datos en la db
			arregloPasajeros = self.buscar(pasajero.getNombre(),
					pasajero.getApellido(),
					pasajero.getDocumento().getTipo().getId(),
					pasajero.getDocumento().getCodigo())

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
		gestordb.guardarObjeto(pasajero)

	
	def construirPasajero(self, dtoPasajero):

		# Se mapea el dto a un objeto pasajero

		# Le pedimos al gestor de direccion que contruya un objeto direccion
		# y lo llene con la informacion del dto
		gestorDir = GestorDireccion()
		direccion = gestorDir.crearDireccion(dtoPasajero)
		
		# Obtenemos informacion necesaria de la db
		# Utilizando sus ids
		gestordb = GestorDB()

		# Con el '[0]' obtenemos el unico elemento que contiene la lista
		ocupacion = gestordb.getObjs(Ocupacion, {'id_ocupacion':dtoPasajero.id_ocupacion})[0]
		nacionalidad = gestordb.getObjs(Nacionalidad, {'id_nacionalidad':dtoPasajero.id_nacionalidad})[0]
		iva = gestordb.getObjs(Iva, {'id_iva':dtoPasajero.id_iva})[0]
		tipoDocu = gestordb.getObjs(TipoDocumento, {'id_tipo':dtoPasajero.id_tipo})[0]

		# Creamos objetos pertinentes
		documento = Documento(codigo=dtoPasajero.getCodigo(), tipo=tipoDocu)

		pasajero = Pasajero(documento=documento,
				direccion=direccion,
				nacionalidad=nacionalidad,
				ocupacion=ocupacion,
				iva=iva,
				**dtoPasajero.atributosPasajero)

		return pasajero
