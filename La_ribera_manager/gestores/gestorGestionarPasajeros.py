#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import Pasajero, Documento, Iva, Ocupacion, Pais,Nacionalidad
from db.gestordb import GestorDB
from db.pipeline import Pipe
from objetos.dtopasajero import dtoPasajero
#from gestordireccion import GestorDireccion

class GestorGestionarPasajeros:
	def buscar(self, nombre, apellido, tipoDocu, documento):
		gestordb = GestorDB()

		return gestordb.buscarPasajero(nombre, apellido, tipoDocu, documento)
	
	def crearPasajero(self, dtoPasajero):	
<<<<<<< HEAD
		omisiones = self.completo(dtoPasajero)
		if not omisiones:
=======
		#if self.completo(dtoPasajero):
>>>>>>> 1f9f1e2e59037cf9fc3bd50c2140568087ad5d7d
		
			# Llamamos al gestor de direcciones
			#gestorDireccion = GestorDireccion()
			#direccion_aux = gestorDireccion.crearDireccion(dtoPasajero)

			#mapea atributos dto con pasajero
		pipe = Pipe()
		keys = dtoPasajero.atributosPasajero.keys()
		p1 = Pasajero()
		for a in keys:
			p1.a = dtoPasajero.atributosPasajero[a]
		
		p1.id_nacionalidad = dtoPasajero.id_nacionalidad
		p1.nacionalidad = pipe.instanciaObjetoID(Nacionalidad,dtoPasajero.id_nacionalidad)
		p1.id_ocupacion = dtoPasajero.id_ocupacion
		p1.ocupacion = pipe.instanciaObjetoID(Ocupacion,dtoPasajero.id_ocupacion) 
		p1.id_iva = dtoPasajero.id_iva
		
		
		
		
		#gestor = GestorDB()
		#gestor.guardarPasajero(p1)
				
			# Llamamos al gestor de base de datos y obtenemos una lista de pasajeros
<<<<<<< HEAD
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
=======
		#gestordb = GestorDB()
		#arregloPasajeros = self.obtenerPasajero(pasajero) 
			
		#if existePasajero(arregloPasajeros):
		#	return False
		#else:
		#	completarCarga(pasajero)
		#	return True

		#else:
			#return faltantes(dtoPasajero)
>>>>>>> 1f9f1e2e59037cf9fc3bd50c2140568087ad5d7d
		

	def completo(self, dtoPasajero):
		# Hacemos una lista con las omisiones
		omisiones=list()
		
		for atributo in dtoPasajero.atributosPasajero:
			print dtoPasajero.atributosPasajero[atributo],atributo
			#if not atributo.startiwith("id"):
			
				
			#for elemento in atributo:
				#if not elemento.startwith("id"):
					#if elemento is None or elemento is "" :
						#omisiones.append(atributo)

		#return omisiones

#probando de guardar cosas en la bd
#gestor = GestorGestionarPasajeros()
#pais = Pais()
#pais.id_pais = 5
#pais.nombrePais = "Jamaica"

#gestor = GestorDB()
#gestor.guardarPasajero(pais)

<<<<<<< HEAD
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
=======
>>>>>>> 1f9f1e2e59037cf9fc3bd50c2140568087ad5d7d
