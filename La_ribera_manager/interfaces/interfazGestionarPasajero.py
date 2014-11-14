#### Interjfaz Gestionar Pasajero ####

import sys, os, inspect

#Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk
from gestores.gestorGestionarPasajeros import GestorGestionarPasajeros
from gestores.gestordireccion import GestorDireccion

class interfazGestionarPasajero:
	def __init__(self):
		
		builder = Gtk.Builder()
		# Dibuja ventanas desde .xml
		builder.add_from_file("Gestionar_Pasajero3.4.xml")
		
		# Obtenemos ventanas
		self.window1 = builder.get_object("window1")
		self.bSiguiente = builder.get_object("bSiguiente")
		self.bCancelar = builder.get_object("bCancelar")
		self.eNombre = builder.get_object("eNombre")
		self.eApellidos = builder.get_object("eApellidos")
		self.eDocumento = builder.get_object("eDocumento")
		self.cDocumento = builder.get_object("cDocumento")
		self.lDocumento = builder.get_object("lDocumento")
		
		self.window1.set_border_width(25)
		self.window1.set_default_size(735,530)

		# Events handlers
		handlers = {
		"on_bSiguiente_clicked": self.on_bSiguiente_clicked,
		"on_window1_destroy": Gtk.main_quit,
		"on_bCancelar_clicked": self.on_bCancelar_clicked,
		"on_cDocumento_changed": self.on_cDocumento_changed,
		}
		builder.connect_signals(handlers)
		
		self.tipo = None
		gestorDireccion = GestorDireccion()
		gestorDireccion.cargarDocumento(self.lDocumento)		
		
		self.window1.show_all()	
		
	def on_bSiguiente_clicked(self,boton):
		nombre = self.eNombre.get_text()
		apellido = self.eApellidos.get_text()
		codigo = self.eDocumento.get_text()
		
		gestionarPasajeros = GestorGestionarPasajeros()
		
		# Comprobamos el contenido del arreglo de pasajeros
		coleccionPasajeros = gestionarPasajeros.buscar(nombre, apellido, tipo, codigo)	
		#if isnull(coleccionPasajeros):
			## llamamos alta pasajero
		#else
			## seleccionamos pasajero y llamamos a modificar pasajero
			## sino selecciona llamamos a dar alta

			
	def on_bCancelar_clicked(self,boton):
		print "cancelar"
			
	def on_cDocumento_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.tipo = id_object
		
	def isnull(coleccionPasajeros):
		return not coleccionPasajeros	

interfazGestionarPasajero()
Gtk.main()	
