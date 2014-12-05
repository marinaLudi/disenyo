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
	def buscar(self, nombre=None, apellido=None, tipoDocu=None, documento=None):
		gestordb = GestorDB()

		arregloPasajeros = gestordb.buscarPasajero(nombre, apellido, tipoDocu, documento)
		
		# Comprobamos si la lista tiene algun pasajero 
		# En caso de que contenga al menos un pasajero se devuelve la lista
		# Si la lista esta vacia se devuelve False
		if self.existePasajero(arregloPasajeros) == True:
			return arregloPasajeros
		else:
			return False

	
	def crearPasajero(self, dtoPasajero):	
			
		# Comprobamos si el usuario omitio algun dato

		omisiones = self.completo(dtoPasajero)
		print omisiones
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

		contenidoDto = [dtoPasajero.getAtributosPasajero(),
				dtoPasajero.getAtributosDireccion(),
				dict(codigo = dtoPasajero.getCodigo(),
					id_tipo = dtoPasajero.getIdTipo(),
					id_localidad = dtoPasajero.getIdLocalidad(),
					id_provincia = dtoPasajero.getIdProvincia(),
					id_pais = dtoPasajero.getIdPais(),
					id_ocupacion = dtoPasajero.getIdOcupacion(),
					id_nacionalidad = dtoPasajero.getIdNacionalidad(),
					id_iva = dtoPasajero.getIdIva())]	

		for atributo in contenidoDto: 
			for atrName, value in atributo.iteritems():
				# Checkeamos los atributos que esten vacios 
				# y no sean opcionales
				if value is None:
					if not self.opcional(atrName):
						omisiones.append(atrName)
					

		return omisiones

	def opcional(self, nombreAtr):
		if nombreAtr is 'cuit'\
				or nombreAtr is 'email'\
				or nombreAtr is 'piso'\
				or nombreAtr is 'dpto':

			return True
		else:
			return False

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
		ocupacion = gestordb.getObjetoID(Ocupacion,dtoPasajero.id_ocupacion)
		nacionalidad = gestordb.getObjetoID(Nacionalidad,dtoPasajero.id_nacionalidad)
		iva = gestordb.getObjetoID(Iva,dtoPasajero.id_iva)
		tipoDocu = gestordb.getObjetoID(TipoDocumento,dtoPasajero.id_tipo)

		# Creamos objetos pertinentes
		documento = Documento(codigo=dtoPasajero.getCodigo(), 
				id_tipo=dtoPasajero.getIdTipo(), 
				tipo=tipoDocu)

		pasajero = Pasajero(
				documento=documento,
				direccion=direccion,
				nacionalidad=nacionalidad,
				ocupacion=ocupacion,
				iva=iva,
				**dtoPasajero.atributosPasajero)

		return pasajero

#probando de guardar cosas en la bd
#gestor = GestorGestionarPasajeros()
#dto = DtoPasajero(nombre="rocio",apellido="lopez",telefono=4550642,codigo=360574845,id_tipo=1,email="ro@hotmail.com",CP=3000,calle="ramirez",id_iva=2,id_nacionalidad=1,id_ocupacion=1,numero=29,dpto="A",piso=2,id_localidad=1,id_provincia=1,id_pais=1,cuit=15,fecha_de_nac="26/12/1992")
#gestor.crearPasajero(dto)

