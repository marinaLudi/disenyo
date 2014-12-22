#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import Pasajero, Documento, Iva, Ocupacion, Pais, Nacionalidad, TipoDocumento
from db.gestordb import GestorDB, Singleton
from objetos.dtopasajero import DtoPasajero
from gestordireccion import GestorDireccion
from datetime import date
import re

# Globals
dni_codigo = None

class GestorGestionarPasajeros:
	def buscar(self, tipoDocu=None, documento=None,nombre=None,apellido=None):
		gestordb = GestorDB()
		arregloPasajeros = gestordb.buscarPasajero(tipoDocu=tipoDocu,
				codigo=documento,
				nombre=nombre,
				apellido=apellido)

		# Comprobamos si la lista tiene algun pasajero
		# En caso de que contenga al menos un pasajero se devuelve la lista
		# Si la lista esta vacia se devuelve False
		if self.existePasajero(arregloPasajeros):
			return arregloPasajeros
		else:
			return False

	
	def crearPasajero(self, dtoPasajero):	
		# Corroboramos si hay un pasajero con los mismos datos en la db
		arregloPasajeros = self.buscar(tipoDocu=dtoPasajero.getIdTipo(),
				documento=dtoPasajero.getCodigo())

		# Creamos el objeto pasajero
		pasajero = self.construirPasajero(dtoPasajero)	


		if self.existePasajero(arregloPasajeros):
			print arregloPasajeros[0].getNombre()
			return False
		else:
			self.completarCarga(pasajero)
			return True
		



	def correcto(self, contenido, test_func):
		# Hacemos una lista con los errores  
		errores=list()
		tipo = list()



		for atributo in contenido:
			for atrName, value in atributo.iteritems():
				# Checkeamos los atributos que esten vacios
				# y no sean opcionales

				if test_func(value, atrName):
					errores.append(atrName)
					
		
		return errores


	def omitido(self, valor, atrName):
		# Comprobamos si el valor del campo es una lista vacia, una cadena vacia
		if not self.opcional(atrName):
			return not valor

	
	def erroneo(self, valor, atrName):

		# Comprobamos que no haya errores de escritura
		if atrName == 'nombre' or atrName == 'apellido':
			return not self.checkNombre(valor)

		elif atrName == 'codigo':
			global dni_codigo
			dni_codigo = valor

		elif atrName == 'cuit' and valor is not None:
			return not self.checkCuit(valor, dni_codigo)

		elif atrName == 'email' and valor is not None:
			return not  self.checkEmail(valor)

		elif atrName == 'CP':
			return not self.checkCP(valor)

		elif atrName == 'dpto' and valor is not None:
			return not self.checkDpto(valor)

		elif atrName == 'piso' and valor is not None:
			return not self.checkPiso(valor)

		else:
			# Estos valores no tendran errores
			return False


	def checkNombre(self, nombre):
		largo = len(nombre)
		
		if largo >= 3 and largo <= 30:
			if re.match(r'^(([a-z]+)(\s[a-z]+)*)$', nombre, re.I):
				return True
			else:
				return False
		else:
			return False


	def checkCuit(self, cuit, dni):

		# Chequemos si la forma del documento es la de un dni
		if self.checkDNI(dni):
			tipo = r'\d{2}'
			codigo = r'\d{8}'
			confirm = r'\d'
			cuit_pattern = r'^%s\-(%s)\-%s$' % (tipo, codigo, confirm)

			# Comprobamos que el cuit tenga la forma estipulada
			# y que la parte central sea igual al dni
			matchObj = re.match(cuit_pattern, cuit)

			if matchObj and matchObj.group(1) == dni:
				return True

			else:
				return False

		else:
			return False


	def checkDNI(self, dni):
		if re.match(r'^\d{8}$', dni):
			return True

		else:
			return False

		
	def checkEmail(self, email):
		atom = r'[\w<>!#\$%&\'*\+\-\/\=\?\^_`\{\|\}~]'
		dot_atom = r'\.%s' % atom
		local_part = r'%s+(%s+)*' % (atom, dot_atom)
		domain = r'%s+(%s+)+' % (atom, dot_atom)
		addr_spec = r'^(%s)@(%s)$' % (local_part, domain)

		if re.match(addr_spec, email, re.I):
			return True

		else:
			return False

	
	def checkCP(self, cp):
		if re.match(r'^\d{3,9}$', cp):
			return True
		
		else:
			return False
			

	def checkDpto(self, dpto):
		if re.match(r'^[a-z]$', dpto):
			return True

		else:
			return False

	
	def checkPiso(self, piso):
		if re.match(r'^\d{1,163}$', piso):
			return True
		
		else:
			return False


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
		

	def checkentries(self, dtopasajero):
		# Obtenemos contenido del dto
		contenidoDto = [dict(codigo = dtoPasajero.getCodigo(),
					id_tipo = dtoPasajero.getIdTipo(),
					id_localidad = dtoPasajero.getIdLocalidad(),
					id_provincia = dtoPasajero.getIdProvincia(),
					id_pais = dtoPasajero.getIdPais(),
					id_ocupacion = dtoPasajero.getIdOcupacion(),
					id_nacionalidad = dtoPasajero.getIdNacionalidad(),
					id_iva = dtoPasajero.getIdIva()),
				dtoPasajero.getAtributosPasajero(),
				dtoPasajero.getAtributosDireccion()]	

		# Checkeamos que no se hayan hecho omisiones en la carga
		omisiones = self.correcto(contenidoDto, self.omitido)

		if omisiones:
			# Devolvemos omisiones
			return omisiones, False

		else:
			# Comprobamos que los campos esten correctamente ingresados
			errores = self.correcto(contenidoDto, self.erroneo)

			if errores:
				# Devolvemos errores
				return errores, True

			
			else:
				# Si no tiene errores ni omisiones
				return [], None

