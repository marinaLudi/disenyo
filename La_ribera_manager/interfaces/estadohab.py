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

		# Obtenemos ventana
		self.window = builder.get_object("window")

		# Obtenemos combos de la interfaz 
		self.dia_ini_combo = builder.get_object("dia_ini_combo")
		self.mes_ini_combo = builder.get_object("mes_ini_combo")
		self.ano_ini_combo = builder.get_object("ano_ini_combo")

		self.dia_fin_combo = builder.get_object("dia_fin_combo")
		self.mes_fin_combo = builder.get_object("mes_fin_combo")
		self.ano_fin_combo = builder.get_object("ano_fin_combo")

		# Gestorcombos se ocupa de cargar los combos con info 
		self.gestorCombos = GestorCombos()
		
		self.gestorCombos.initDateCombo(self.dia_ini_combo,
				self.mes_ini_combo,
				self.ano_ini_combo)

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
			"onButtonClicked": self.mostrarHabitaciones,
			"onComboIniChanged": self.comboIniChanged,
			"onComboFinChanged": self.comboFinChanged
		}
		builder.connect_signals(handlers)

		# Monstramos ventana
		self.window.show_all()
	

	def comboIniChanged(self, combo):
		self.gestorCombos.comboUpDate(self.dia_ini_combo, 
				self.mes_ini_combo, 
				self.ano_ini_combo)


	def comboFinChanged(self, combo):
		self.gestorCombos.comboUpDate(self.dia_fin_combo, 
				self.mes_fin_combo, 
				self.ano_fin_combo)


	def mostrarHabitaciones(self, combo):
		fecha_ini = self.gestorCombos.getDate(self.dia_ini_combo,
				self.mes_ini_combo,
				self.ano_ini_combo)		


		fecha_fin = self.gestorCombos.getDate(self.dia_fin_combo,
				self.mes_fin_combo,
				self.ano_fin_combo)

		
		if self.validarFecha(fecha_ini, fecha_fin):

		else:
			print "Fecha ini > fin >:^("	
		

	def validarFecha(self, ini, fin):
		return fin > ini


InterfazEstadoHabitacion()
Gtk.main()
		
