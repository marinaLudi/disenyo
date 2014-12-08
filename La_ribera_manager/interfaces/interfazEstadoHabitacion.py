#!/usr/bin/python
#### Interfaz Mostrar Estado Habitacion ####

import sys, os, inspect

# Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk, Gdk
from gestores.gestorcombos import GestorCombos
from gestores.mostrarhabitacion import GestorMostrarEstado
from datetime import timedelta,date,datetime

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

	def armarGrilla(self,fecha_inicio,fecha_fin):
		
		gestor_estado = GestorMostrarEstado()
			
		window = Gtk.Window()
		scrolled_window = Gtk.ScrolledWindow()
		scrolled_window.set_policy(Gtk.PolicyType.AUTOMATIC, Gtk.PolicyType.ALWAYS)
		scrolled_window.set_min_content_height(VENTANA_ANCHO)
		scrolled_window.set_min_content_width(VENTANA_ALTO)
		window.set_border_width(BORDE_ANCHO)
		window.set_default_size(VENTANA_ALTO, VENTANA_ANCHO)
		grid = Gtk.Grid()
		window.add(grid)
		grid.add(scrolled_window)

					
		#crea la lista de donde va a tomar las cosas el toggle, el boolean activado o no
		#los colores seria rojo=ocupada, azul=libre y amarillo=reservada
		#la ultima columna seria la fecha
		self.store = Gtk.ListStore(str)
		
		for date in self.daterange(fecha_inicio, fecha_fin):
			treeiter = self.store.append([str(date)])
				
		tree = Gtk.TreeView(self.store)
		renderer = Gtk.CellRendererText()

		column = Gtk.TreeViewColumn("Fecha\hab", renderer,text=0)
		tree.append_column(column)
				
		habitaciones = [101,102,201,202]
		self.stores = []
		columns = []
		renderers = []
		num = 0
		for e in habitaciones:
			self.stores.append(Gtk.ListStore(bool,str,str))
			
			for fecha in self.daterange(fecha_inicio, fecha_fin):
				color = gestor_estado.estadoHabitacion(fecha,e)
				self.stores[num].append([False,color,str(fecha)])
				
			renderers.append(Gtk.CellRendererToggle())
			columns.append(Gtk.TreeViewColumn(str(e), renderers[num]))
			columns[num].set_cell_data_func(renderers[num], self.inIta, self.stores[num])
			tree.append_column(columns[num])
			renderers[num].connect("toggled", self.on_cell_toggled,num)
		
			num = num + 1	

		self.fecha_ini = None
		self.fecha_fin = None
		
		for a in self.stores:
			for b in self.daterange(fecha_inicio, fecha_fin):
				a[0]

		scrolled_window.add(tree)
		window.show_all()
		
	def on_cell_toggled(self, widget, path,num):
		print num,path
		if self.fecha_ini is None:
			self.fecha_ini = self.stores[num][int(path)][2]
			self.stores[num][int(path)][0] = not self.stores[num][int(path)][0]
			print self.fecha_ini
		elif self.fecha_fin is None:
			self.fecha_fin = self.stores[num][int(path)][2]
			self.stores[num][int(path)][0] = not self.stores[num][int(path)][0]
			print self.fecha_fin
		else:
			self.fecha_ini=None
			self.fecha_fin=None
			
	
	def inIta(self,col, cell, model, iter, mymodel):
		s = model.get_string_from_iter(iter)
		niter = mymodel.get_iter_from_string(s)
		obj = mymodel.get_value(niter, 0)
		back = mymodel.get_value(niter,1)
		cell.set_property('active', obj)
		cell.set_property('cell-background',back)
	
	def daterange(self,start_date, end_date):
		for n in range(int ((end_date - start_date).days)):
			yield start_date + timedelta(n)





inter=InterfazEstadoHabitacion()
inter.armarGrilla(date(2014, 12, 1),date(2014, 12, 25))
Gtk.main()
