import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.gestordb import GestorDB, Singleton
from db.models import Direccion, Localidad, Provincia, Pais
from objetos.dtopasajero import DtoPasajero

class GestorDireccion:
	
	def crearDireccion(self, dtoPasajero):
		
		# Se mapea del dto a un objeto direccion
		# Obtenemos los datos necesarios de la db
		gestordb = GestorDB()
		verif = gestordb.getObjs(Direccion,**dtoPasajero.atributosDireccion)
		if verif:
			return verif[0]
		else:	
			localidad = gestordb.getObjetoID(Localidad, dtoPasajero.id_localidad)
	
			# Creamos y llenamos el objeto direccion
			direccion = Direccion(localidad=localidad, **dtoPasajero.atributosDireccion)
			return direccion


