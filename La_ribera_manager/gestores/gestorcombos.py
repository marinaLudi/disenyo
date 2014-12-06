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
ANO_MIN = 1930
ANO_MAX = date.today().year

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
		self.upDateCombos([combo_dia, combo_mes, combo_ano],
				[day_range, month_range, year_range])
			

	def dateChange(self, diaCombo, mesCombo, anoCombo, diaOpuesto, mesOpuesto, anoOpuesto, flag):

		dia = int(diaCombo.get_active_text())
		mes = int(mesCombo.get_active_text())
		ano = int(anoCombo.get_active_text())

		dopuesto = int(diaOpuesto.get_active_text())
		mopuesto = int(mesOpuesto.get_active_text())
		aopuesto = int(anoOpuesto.get_active_text())

		# El valor flag == 1 indica que el combo cambiado es el combo de fecha incio 
		# y el opuesto el de fecha fin
		if flag is 1:
			year_range = (ANO_MIN, aopuesto)

			if ano == aopuesto:
				month_range = (1, mopuesto)

				if mes == mopuesto:
					day_range = (1, dopuesto)

				else:
					day_range = (1, calendar.monthrange(ano, mes)[1])

			else:
				month_range = (1, 12)
				day_range = (1, calendar.monthrange(ano, mes)[1])

		elif flag is -1:
			year_range = (aopuesto, ANO_MAX)

			if ano == aopuesto:
				month_range = (mopuesto, 12)

				if mes == mopuesto:
					day_range = (dopuesto,
							calendar.monthrange(aopuesto, mopuesto)[1])

				else:
					day_range = (1, calendar.monthrange(aopuesto, mopuesto)[1])

			else:
				month_range = (1, 12)
				day_range = (1, calendar.monthrange(aopuesto, mopuesto)[1])


		# Actualizamos los valores de los combos
		self.upDateCombos([diaCombo, mesCombo, anoCombo],
				[day_range, month_range, year_range])


	def upDateCombos(self, combos, rangos):
		for combo, rango in izip(combos, rangos):
			combo.remove_all()

			for valor in range(rango[0], rango[1] + 1):
				combo.append_text(str(valor))

	
	def setActive(self, combos, valoresActivos):
		for combo, valor in izip(combos, valoresActivos):
			combo.set_active(valor)
	


		

		
