# -*- coding: utf-8 -*-
#### Interfaz Gestionar Pasajero ####

import sys, os, inspect

# Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk
from gestores.gestorGestionarPasajeros import GestorGestionarPasajeros
from gestores.gestordireccion import GestorDireccion
from gestores.gestorcombos import GestorCombos
from gestores.gestordialogos import GestorDialogos
from gestores.gestorOcuparHab import GestorOcuparHab
from interfaces.interfazDarAltaPasajero import InterfazDarAltaPasajero
import interfaces.interfazEstadoHabitacion

# Globals
BORDE_ANCHO = 25
VENTANA_ALTO = 530
VENTANA_ANCHO = 735

class InterfazOcuparHabitacion:
	def __init__(self,fecha_inicio,fecha_fin,habitacion):
		
		builder = Gtk.Builder()

		# Dibuja ventanas desde .xml
		builder.add_from_file("Gestionar_Pasajero3.4.xml")
		
		# Obtenemos widgets
		self.window1 = builder.get_object("window1")
		self.bSiguiente = builder.get_object("bSiguiente")
		self.bCancelar = builder.get_object("bCancelar")
		self.eNombre = builder.get_object("eNombre")
		self.eApellido = builder.get_object("eApellido")
		self.eDocumento = builder.get_object("eDocumento")
		self.cDocumento = builder.get_object("cDocumento")
		self.lDocumento = builder.get_object("lDocumento")
		
		self.window1.set_border_width(BORDE_ANCHO)
		self.window1.set_default_size(VENTANA_ANCHO, VENTANA_ALTO)

		# Obtenemos informacion para los combos desde la db
		self.gestorCombos = GestorCombos()
		self.gestorCombos.cargarCombos(lDocumento=self.lDocumento)
		
		self.dialogos = GestorDialogos()
		self.gestorOcuparHab = GestorOcuparHab()


		# Events handlers
		handlers = {
		"on_bSiguiente_clicked": self.on_bSiguiente_clicked,
		"on_window1_destroy": Gtk.main_quit,
		"on_bCancelar_clicked": self.on_bCancelar_clicked,
		"on_cDocumento_changed": self.on_cDocumento_changed,
		}
		builder.connect_signals(handlers)
		
		# Variable auxiliar
		self.tipo = None
		self.pasajero = None
		self.habitacion = habitacion
		self.fecha_inicio = fecha_inicio
		self.fecha_fin = fecha_fin

		# Monstramos la ventana con los widgets
		self.window1.show_all()	
		

	def on_bSiguiente_clicked(self, boton):
		# Obtenemos informacion de la interfaz
		nombre = self.eNombre.get_text()
		apellido = self.eApellido.get_text()
		codigo = str(self.eDocumento.get_text())
		if nombre is '':
			nombre=None
		if apellido is '':
			apellido = None
		if codigo is '':
			codigo = None

		
		# Buscamos pasajero
		gestionarPasajeros = GestorGestionarPasajeros()
		arregloPasajeros = gestionarPasajeros.buscar(nombre, apellido,self.tipo,codigo)



		if not arregloPasajeros:
			# Se genera la intefaz de dar alta pasajero
			darAlta = InterfazDarAltaPasajero()
			self.window1.hide()

		else:
			# Se muestra en la pantalla la grilla para seleccionar al pasajero
			pasajero = self.seleccionarPasajero(arregloPasajeros)
		

			
	def on_bCancelar_clicked(self, boton):
		Gtk.main_quit()
		

	def on_cDocumento_changed(self, combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.tipo = id_object
			
		

	def seleccionarPasajero(self,arregloPasajeros):
		self.window1.hide()
	
		builder = Gtk.Builder()
		
		builder.add_from_file("ocupar_habitacion.xml")
		self.window2 = builder.get_object("window2")
		lPasajeros = builder.get_object("lPasajeros")
		bAceptar = builder.get_object("Aceptar")
		treeView = builder.get_object("treeviewLista")
		rResponsable = builder.get_object("radiobutton1")
		rAcompanyante = builder.get_object("radiobutton2")
		
		handlers = {
		"on_window2_destroy": Gtk.main_quit}
		builder.connect_signals(handlers)

		
		self.window2.set_border_width(BORDE_ANCHO)
		self.window2.set_default_size(VENTANA_ANCHO, VENTANA_ALTO)
				
		for e in arregloPasajeros:
				lPasajeros.append([e.getNombre(),e.getApellido(),e.getDocumento().getTipo().getTipo(),e.getDocumento().getCodigo(),e.getId()])
		
		select = treeView.get_selection()
		
		self.tipoPasajero = 'responsable'
	
		select.connect("changed", self.on_tree_selection_changed)
		bAceptar.connect("clicked", self.on_Aceptar_clicked,self.window2,treeView)
		rResponsable.connect("toggled", self.on_radio_toggled, "responsable")
		rAcompanyante.connect("toggled", self.on_radio_toggled, "acompanyante")
		
		self.window2.show_all()
	
	def on_Aceptar_clicked(self,boton,window,treeView):
		# El usuario elige un pasajero
		if self.pasajero is not None:
			respuesta = self.dialogos.pregunta("¿Que desea hacer?","Seguir Cargando","Cargar otra habitación","Salir")
			if respuesta == Gtk.ResponseType.YES:
				print type(self.fecha_inicio)
				self.gestorOcuparHab.ocuparHab(self.pasajero,self.tipoPasajero,self.habitacion,self.fecha_inicio,self.fecha_fin)
				self.window2.hide()
				self.window1.show_all()
			elif respuesta == Gtk.ResponseType.NO:
				interfaces.interfazEstadoHabitacion.InterfazEstadoHabitacion()
				self.window2.hide()
				
			elif respuesta == Gtk.ResponseType.CLOSE:
				Gtk.main_quit()

		
	
	def on_tree_selection_changed(self,selection):
		model,treeiter = selection.get_selected()
		if treeiter is not None:
			 self.pasajero = model[treeiter][0]
			 
	def on_radio_toggled(self, button, name):
		if button.get_active():
			self.tipoPasajero = name
			 
if __name__ == '__main__':		
	InterfazOcuparHabitacion()
	Gtk.main()		
		

