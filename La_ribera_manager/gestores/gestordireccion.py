import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.gestordb import GestorDB, Singleton
from db.models import Direccion, Localidad, Provincia, Pais

class GestorDireccion:
	
	def crearDireccion(self, dtoPasajero):
		
		# Se mapea del dto a un objeto direccion
		# Obtenemos los datos necesarios de la db
		gestordb = GestorDB()

		# Con el [0] obtenemos el unico elemento de la lista que devuelve el mensaje
		localidad = gestordb.getObjs(Localidad, {'id_localidad':dtoPasajero.id_localidad})[0]

		# Creamos y llenamos el objeto direccion
		direccion = Direccion(localidad=localidad, **dtoPasajero.atributosDireccion)

		return direccion
		
		

