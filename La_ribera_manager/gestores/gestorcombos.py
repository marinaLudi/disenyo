import sys, os, inspect

currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

#Globals
NOFILTER = {}

from db.gestordb import GestorDB, Singleton
from db.models import Nacionalidad, Ocupacion, Iva, Pais, Documento
import calendar
from datetime import date

class GestorCombos:
	def cargarCombos(self, *tuplas):
		gestordb = GestorDB()

		# Cada uno de los elementos en la lista 'tuplas' tiene la forma (objeto, combo)
		for elem in tuplas:

			# Con el 'objeto' se obtienen todas las filas de la tabla requerida
			filas = gestordb.getObjs(elem[0], NOFILTER)

			# Con los atributos de cada uno de los objetos se cargan los combos
			for objeto in filas:
				elem[1].append(objeto.pack())


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



