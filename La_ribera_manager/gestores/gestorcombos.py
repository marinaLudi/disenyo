import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from db.gestordb import GestorDB, Singleton
from db.models import Nacionalidad, Ocupacion, Iva, Pais, Documento

	def cargarCombos(self,lPais,lNacionalidad,lOcupacion,lIVA):
		#############################################################
		#############################################################
		pipe = Pipe()
		
		paises = pipe.cargarCombo(Pais)
		for e in paises:
			lPais.append([e.id_pais, e.nombrePais])
		
		nacionalidades = pipe.cargarCombo(Nacionalidad)
		for e in nacionalidades:
			lNacionalidad.append([e.id_nacionalidad,e.nombreNacionalidad])
		
		ocupaciones = pipe.cargarCombo(Ocupacion)	
		for e in ocupaciones:
			lOcupacion.append([e.id_ocupacion,e.descripcion_ocupacion])							

		ivas = pipe.cargarCombo(Iva)
		for e in ivas:
			lIVA.append([e.id_iva,e.descripcion_iva])
			
	
	def getProvincia(self, lProvincia, id_pais):
		pipe = Pipe()
		pipe.getProvincia(lProvincia, id_pais)
	
	def getLocalidad(self, lLocalidad, id_provincia):
		pipe= Pipe()
		pipe.getLocalidad(lLocalidad, id_provincia)	
		
	def cargarDocumento(self, lDocumento):
		pipe= Pipe()
		documentos = pipe.cargarCombo(Documento)
		for e in documentos:
			lDocumento.append([e.codigo,e.tipo])
		############################################################
		############################################################
