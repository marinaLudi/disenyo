import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


from db.gestordb import GestorDB, Singleton
<<<<<<< HEAD
from db.models import Nacionalidad, Ocupacion, Iva, Pais, Documento
import calendar
from datetime import date



from db.models import Nacionalidad, Ocupacion, Iva, Pais, TipoDocumento, Provincia, Localidad

class GestorCombos:
	def __init__(self):
		self.gestordb = GestorDB()

	def cargarCombos(self, 
			lPais=None, 
			lNacionalidad=None, 
			lOcupacion=None, 
			lIVA=None, 
			lDocumento=None):

		if lPais is not None:
			paises = self.gestordb.getTabla(Pais)
			for e in paises:
				lPais.append([e.id_pais,e.nombrePais])
				
		if lNacionalidad is not None:
			nacionalidades = self.gestordb.getTabla(Nacionalidad)
			for e in nacionalidades:
				lNacionalidad.append([e.id_nacionalidad,e.nombreNacionalidad])

		if lOcupacion is not None:
			ocupaciones = self.gestordb.getTabla(Ocupacion)
			for e in ocupaciones:
				lOcupacion.append([e.id_ocupacion,e.descripcion_ocupacion])

		if lIVA is not None:
			ivas = self.gestordb.getTabla(Iva)
			for e in ivas:
				lIVA.append([e.id_iva,e.getDescripcion()])

		if lDocumento is not None:		
			documentos = self.gestordb.getTabla(TipoDocumento)
			for e in documentos:
				lDocumento.append([e.id_tipo,e.tipo])
		

	def getProvincia(self, lProvincia, id_pais):
		lProvincia.clear()
		provincias = self.gestordb.getTablaID(Provincia,'id_pais',id_pais)
		for e in provincias:
			lProvincia.append([e.id_provincia,e.nombreProv])

		
	def getLocalidad(self,lLocalidad,id_provincia):
		lLocalidad.clear()
		localidades = self.gestordb.getTablaID(Localidad,'id_provincia',id_provincia)
		for e in localidades:
			lLocalidad.append([e.id_localidad,e.nombreLocalidad])


	def initDateCombo(self, combo_dia, combo_mes, combo_ano):
		# seteamos rango de anos y meses
		year_range = (1930, date.today().year)
		month_range = (1, 12)

		# Cargamos los combos con los anos, meses y dias correspondientes
		for year in range(year_range[0], year_range[1] + 1):
			combo_ano.append_text(str(year))

		for month in range(month_range[0], month_range[1] + 1):
			combo_mes.append_text(str(month))

		day_range = (1, calendar.monthrange(year, month)[1]) 
		for day in range(day_range[0], day_range[1] + 1):
			combo_dia.append_text(str(day))
