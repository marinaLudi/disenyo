#### Gestor Gestionar Pasajeros ####

import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.models import *
from db.gestordb import GestorDB
from db.pipeline import Pipe
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
		pipe = Pipe()
		keys = dtoPasajero.atributosPasajero.keys()
		p1 = Pasajero()
		for a in keys:
			p1.a = dtoPasajero.atributosPasajero[a]
			print p1.a,a
		
		p1.nombre = dtoPasajero.atributosPasajero['nombre']	
		p1.id_nacionalidad = dtoPasajero.id_nacionalidad
		p1.nacionalidad = pipe.instanciaObjetoID(Nacionalidad,dtoPasajero.id_nacionalidad)
		p1.id_ocupacion = dtoPasajero.id_ocupacion
		p1.ocupacion = pipe.instanciaObjetoID(Ocupacion,dtoPasajero.id_ocupacion) 
		p1.id_iva = dtoPasajero.id_iva
		p1.iva = pipe.instanciaObjetoID(Iva,dtoPasajero.id_iva)
		pais = pipe.instanciaObjetoID(Pais,dtoPasajero.id_pais)
		provincia = pipe.instanciaObjetoID(Provincia,dtoPasajero.id_provincia)
		localidad = pipe.instanciaObjetoID(Localidad,dtoPasajero.id_localidad)
		direccion = Direccion()
		
		
		keys = dtoPasajero.atributosDireccion.keys()
		for e in keys:
			direccion.e = dtoPasajero.atributosDireccion[e]
		direccion.id_localidad = dtoPasajero.id_localidad
		direccion.id_direccion = 1
		
		p1.direccion = direccion 
		p1.id_direccion = direccion.id_direccion	

		d1= Direccion(calle="san martin",numero=3329,dpto="A",piso=2,id_localidad=1)
		pais = Pais(nombrePais="Japon")
		
		gestor = GestorDB()

		gestor.guardarPasajero(pais)
		print d1.calle

		#gestor.guardarPasajero(p1)
				
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
		
	#def completo(self, dtoPasajero):
		#omisiones=list()
		
		#for atributo in dtoPasajero.atributosPasajero:
			#print dtoPasajero.atributosPasajero[atributo],atributo
			#if not atributo.startiwith("id"):
			
				
			#for elemento in atributo:
				#if not elemento.startwith("id"):
					#if elemento is None or elemento is "" :
						#omisiones.append(atributo)

		#return omisiones



#probando de guardar cosas en la bd
gestor = GestorGestionarPasajeros()
dto = dtoPasajero(nombre="marina",apellido="ludi",telefono=4230642,email="mari.627@hotmail.com",CP=3000,calle="san martin",id_iva=1,id_nacionalidad=1,id_ocupacion=2,numero=3329,dpto="A",piso=2,id_localidad=1,id_provincia=1,id_pais=1)
gestor.crearPasajero(dto)
#pais = Pais()
#pais.id_pais = 5
#pais.nombrePais = "Jamaica"
#gestor = GestorDB()
#gestor.guardarPasajero(pais)
