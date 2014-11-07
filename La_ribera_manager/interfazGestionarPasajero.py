from gi.repository import Gtk
from objetos.dtopasajero import DtoPasajero

class interfazGestionarPasajero:
	def __init__(self):
		
		builder = Gtk.Builder()
		builder.add_from_file("interfaces/Gestionar_Pasajero3.4.xml")
		
		self.window1 = builder.get_object("window1")
		self.bSiguiente = builder.get_object("bSiguiente")
		self.bCancelar = builder.get_object("bCancelar")
		self.eNombre = builder.get_object("eNombre")
		self.eApellidos = builder.get_object("eApellidos")
		self.eDocumento = builder.get_object("eDocumento")
		self.cDocumento = builder.get_object("cDocumento")
		
		self.window1.set_border_width(25)
		self.window1.set_default_size(735,530)

		
		handlers = {
		"on_bSiguiente_clicked": self.on_bSiguiente_clicked,
		"on_window1_destroy": Gtk.main_quit,
		"on_bCancelar_clicked": self.on_bCancelar_clicked,
		"on_cDocumento_changed": self.on_cDocumento_changed,
		}
		builder.connect_signals(handlers)
		pasajero = DtoPasajero()
		
		self.window1.show_all()	
		
	def on_bSiguiente_clicked(self,boton):
		pasajero.nombre = self.eNombre.get_text()
		pasajero.apellido = self.eApellidos.get_text()
		pasajero.codigo = self.eDocumento.get_text()
		print "buscar pasajero"
			
	def on_bCancelar_clicked(self,boton):
		print "cancelar"
			
	def on_cDocumento_changed(self,combo):
		print "cargar dni"
		
		
		
interfazGestionarPasajero()
Gtk.main()	
