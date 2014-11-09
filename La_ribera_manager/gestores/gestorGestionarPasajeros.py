#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import Pasajero, Documento, Iva, Ocupacion, Pais
from db.gestordb import GestorDB
from objetos.dtopasajero import dtoPasajero
#from gestordireccion import GestorDireccion

class GestorGestionarPasajeros:
	def buscar(self, nombre, apellido, tipoDocu, Documento):
		gestordb = GestorDB()

		return gestordb.buscarPasajero(nombre, apellido, tipoDocu, Documento)
	
	def crearPasajero(self, dtoPasajero):	
		#if self.completo(dtoPasajero):
		
			# Llamamos al gestor de direcciones
			#gestorDireccion = GestorDireccion()
			#direccion_aux = gestorDireccion.crearDireccion(dtoPasajero)

			#mapea atributos dto con pasajero
		keys = dtoPasajero.atributosPasajero.keys()
		p1 = Pasajero()
		for a in keys:
			p1.a = dtoPasajero.atributosPasajero[a]
		
		gestor = GestorDB()
		gestor.guardarPasajero(p1)
				
			# Llamamos al gestor de base de datos y obtenemos una lista de pasajeros
		#gestordb = GestorDB()
		#arregloPasajeros = self.obtenerPasajero(pasajero) 
			
		#if existePasajero(arregloPasajeros):
		#	return False
		#else:
		#	completarCarga(pasajero)
		#	return True

		#else:
			#return faltantes(dtoPasajero)
		
	def completo(self, dtoPasajero):
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

