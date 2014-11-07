from gi.repository import Gtk
from objetos.dtopasajero import DtoPasajero

class interfazGestionarPasajero:
	def __init__(self):
		
		builder = Gtk.Builder()
		builder.add_from_file("interfaces/Gestionar_Pasajero3.4.xml")
		
		self.window1 = builder.get_object("window1")
		self.bSiguiente = builder.get_object("bSiguiente")
		self.bCancelar = builder.get_object("bCancelar")
		self.eNombres = builder.get_object("eNombre")
		self.eApellidos = builder.get_object("eApellidos")
		self.eDocumento = builder.get_object("eDocumento")
		self.cDocumento = builder.get_object("cDocumento")
		
		self.window1.set_border_width(25)
		self.window1.set_default_size(800,600)

		
		"""handlers = {
		"on_bSiguiente_clicked": self.on_bSiguiente_clicked,
		"on_window1_destroy": Gtk.main_quit,
		"on_bCancelar_clicked": self.on_bCancelar_clicked
		}"""
		
		self.window1.show_all()	
		
interfazGestionarPasajero()
Gtk.main()	
