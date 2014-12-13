import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)


from db.gestordb import GestorDB, Singleton
from db.models import Nacionalidad, Ocupacion, Iva, Pais, Documento, TipoDocumento, Provincia, Localidad

import calendar
from datetime import date
from itertools import izip


# Globals
ano_actual = date.today().year
ANO_MIN = ano_actual - 5
ANO_MAX = ano_actual + 1

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
		year_range = (ANO_MIN, ANO_MAX)
		month_range = (1, 12)
		day_range = (1, calendar.monthrange(ANO_MIN, 1)[1]) 

		# Cargamos los combos con los anos, meses y dias correspondientes
		for combo, rango in izip([combo_dia, combo_mes, combo_ano],
				[day_range, month_range, year_range]):	
			
			for valor in range(rango[0], rango[1] + 1):
				combo.append_text(str(valor))	
			

		
	def comboUpDate(self, comboDia, comboMes, comboAno):
		# Obtenemos ano y mes
		year = int(comboAno.get_active_text())
		month = int(comboMes.get_active_text())

		# Obtenemos rango de dias
		day_range = (1, calendar.monthrange(year, month)[1])
		
		# Limpiamos combo
		comboDia.remove_all()	

		#Llenamos combo
		for dia in range(day_range[0], day_range[1]):
			comboDia.append_text(str(dia))	

	
	def setActive(self, combos, valoresActivos):
		for combo, valor in izip(combos, valoresActivos):
			combo.set_active(valor)
	

	def getDate(self, comboDia, comboMes, comboAno):
		day = int(comboDia.get_active_text())
		month = int(comboMes.get_active_text())
		year = int(comboAno.get_active_text())

		return date(year, month, day)


		
