from gi.repository import Gtk

class interfazPasajero:
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("Cargar_Pasajero3.4.xml")
		
		self.window1 = builder.get_object("window1")
		self.bSiguiente = builder.get_object("bSiguiente")
		self.eNombres = builder.get_object("eNombres")
		self.eApellidos = builder.get_object("eApellidos")
		self.cDocumento = builder.get_object("cDocumento")
		self.cPais = builder.get_object("cPais")
		
		self.window1.set_border_width(25)
		
		handlers = {
		"on_bSiguiente_clicked": "",
		"on_window1_destroy": Gtk.main_quit,
		"on_cPais_changed": "",
		"on_cProvincia_changed": "",
		"on_cLocalidad_changed": "",
		"on_cDocumento_changed": "",
		"on_cNacionalidad_changed": "",
		"on_cAnyo_changed": "",
		"on_cDia_changed": "",
		}
		builder.connect_signals(handlers)
		self.window1.show_all()
		
		
#interfazPasajero()
#Gtk.main()
