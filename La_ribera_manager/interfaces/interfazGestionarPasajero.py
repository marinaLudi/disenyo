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
from interfaces.interfazDarAltaPasajero import InterfazDarAltaPasajero

# Globals
BORDE_ANCHO = 25
VENTANA_ANCHO = 530
VENTANA_ALTO = 735

class InterfazGestionarPasajero:
	def __init__(self):
		
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
		self.window1.set_default_size(VENTANA_ALTO, VENTANA_ANCHO)

		# Obtenemos informacion para los combos desde la db
		self.gestorCombos = GestorCombos()
		self.gestorCombos.cargarCombos(lDocumento=self.lDocumento)

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

		# Monstramos la ventana con los widgets
		self.window1.show_all()	
		

	def on_bSiguiente_clicked(self, boton):
		# Obtenemos informacion de la interfaz
		nombre = self.eNombre.get_text()
		apellido = self.eApellido.get_text()
		codigo = str(self.eDocumento.get_text())
		
		# Buscamos pasajero
		gestionarPasajeros = GestorGestionarPasajeros()
		arregloPasajeros = gestionarPasajeros.buscar(nombre, apellido,  self.tipo,codigo)


		if not arregloPasajeros:
			# Se genera la intefaz de dar alta pasajero
			darAlta = InterfazDarAltaPasajero()
			darAlta.altaPasajero()

		else:
			# Se muestra en la pantalla la grilla para seleccionar al pasajero
			pasajero = self.seleccionarPasajero(arregloPasajeros)
		

			
	def on_bCancelar_clicked(self, boton):
		print "cancelar"
		Gtk.main_quit()
		

	def on_cDocumento_changed(self, combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.tipo = id_object
			
		

	def seleccionarPasajero(self, arregloPasajeros):
		builder = Gtk.Builder()
		
		builder.add_from_file("Lista_pasajeros.xml")
		window2 = builder.get_object("window2")
		lPasajeros = builder.get_object("lPasajeros")
		b2Siguiente = builder.get_object("b2Siguiente")
		
		handlers = {
		"on_b2Siguiente_clicked": self.on_b2Siguiente_clicked,
		"on_window1_destroy": Gtk.main_quit}
		
		window2.set_border_width(BORDE_ANCHO)
		window2.set_default_size(VENTANA_ALTO, VENTANA_ANCHO)		
		for e in arregloPasajeros:
				print e.getNombre()
				lPasajeros.append([e.getNombre(),e.getApellido(),e.getDocumento().getTipo(),e.getDocumento().getCodigo()])
		window2.show_all()
	
	def on_b2Siguiente_clicked(self,boton,pasajero):
		
			if pasajero is None:
				# El usuario no elige ningun pasajero
				darAlta = InterfazDarAltaPasajero()
				darAlta.altaPasajero()

			else:
				# El usuario elige un pasajero
				print "Mod Pasajero"
		
		
		

if __name__ == '__main__':		
	InterfazGestionarPasajero()
	Gtk.main()
