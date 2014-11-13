import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.pipeline import Pipe

class GestorDireccion:
	def cargarCombos(self,lPais,lNacionalidad,lOcupacion,lIVA):
		pipe = Pipe()
		pipe.cargarCombos(lPais,lNacionalidad,lOcupacion,lIVA)
	
	def getProvincia(self, lProvincia, id_pais):
		pipe = Pipe()
		pipe.getProvincia(lProvincia, id_pais)
	
	def getLocalidad(self, lLocalidad, id_provincia):
		pipe= Pipe()
		pipe.getLocalidad(lLocalidad, id_provincia)	
		
	def cargarDocumento(self, lDocumento):
		pipe= Pipe()
		pipe.cargarDocumento(lDocumento)
		
		
		
	
