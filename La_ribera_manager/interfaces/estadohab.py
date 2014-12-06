#!/usr/bin/python
#### Interfaz Mostrar Estado Habitacion ####

import sys, os, inspect

# Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk, Gdk
from gestores.gestorcombos import GestorCombos

# Globals
BORDE_ANCHO = 25
VENTANA_ANCHO = 530
VENTANA_ALTO = 735

class InterfazEstadoHabitacion:
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("estado_habitacion.xml")

		# Obtenemos combos de la interfaz 
		self.dia_ini_combo = builder.get_object("dia_ini_combo")
		self.mes_ini_combo = builder.get_object("mes_ini_combo")
		self.ano_ini_combo = builder.get_object("ano_ini_combo")

		self.dia_fin_combo = builder.get_object("dia_fin_combo")
		self.mes_fin_combo = builder.get_object("mes_fin_combo")
		self.ano_fin_combo = builder.get_object("ano_fin_combo")

		# Gestorcombos se ocupa de cargar los combos con info 
		self.gestorCombos = GestorCombos()
		
		self.dia_ini_combo.append_text("1")		
		self.mes_ini_combo.append_text("1")
		self.ano_ini_combo.append_text("1930")
		self.gestorCombos.initDateCombo(self.dia_fin_combo,
				self.mes_fin_combo,
				self.ano_fin_combo)
		
		# Seteamos items activos
		self.gestorCombos.setActive([self.dia_ini_combo,
			self.mes_ini_combo,
			self.ano_ini_combo,
			self.dia_fin_combo,
			self.mes_fin_combo,
			self.ano_fin_combo],
				[0, 0, 0, 0, 0, 0])

		# Conectamos las senales con sus funciones
		handlers = {
			"onDeleteWindow": Gtk.main_quit,
			"comboDiaIniChanged": self.comboIniChange,
			"comboMesIniChanged": self.comboIniChange,
			"comboAnoIniChanged": self.comboIniChange,
			"comboDiaFinChanged": self.comboFinChange,
			"comboMesFinChanged": self.comboFinChange,
			"comboAnoFinChanged": self.comboFinChange
		}
		builder.connect_signals(handlers)


		# Monstramos ventana
		self.window = builder.get_object("window")
		self.window.show_all()
	

	def comboIniChange(self, combo):
		gestorCombos = GestorCombos()
		
		gestorCombos.dateChange(self.dia_ini_combo,
				self.mes_ini_combo,
				self.ano_ini_combo,
				self.dia_fin_combo,
				self.mes_fin_combo,
				self.ano_fin_combo,
				flag=1)


	def comboFinChange(self, combo):
		gestorCombos = GestorCombos()

		gestorCombos.dateChange(self.dia_fin_combo,
				self.mes_fin_combo,
				self.ano_fin_combo,
				self.dia_ini_combo,
				self.mes_ini_combo,
				self.ano_ini_combo,
				flag=-1)
InterfazEstadoHabitacion()
Gtk.main()
		
