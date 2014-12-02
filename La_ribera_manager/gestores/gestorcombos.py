import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#Globals
NOFILTER = {}

from db.gestordb import GestorDB, Singleton
from db.models import Nacionalidad, Ocupacion, Iva, Pais, Documento

	def cargarCombos(self, *tuplas):
		gestordb = GestorDB()

		# Cada uno de los elementos en la lista 'tuplas' tiene la forma (objeto, combo)
		for elem in tuplas:

			# Con el 'objeto' se obtienen todas las filas de la tabla requerida
			filas = gestordb.getObjs(elem[0], NOFILTER)

			# Con los atributos de cada uno de los objetos se cargan los combos
			for objeto in filas:
				elem[1].append(objeto.pack())


	def getProvincia(self, lProvincia, id_pais):
		# Stuff	

	def getLocalidad(self, lLocalidad, id_provincia):
		# Stuff	
