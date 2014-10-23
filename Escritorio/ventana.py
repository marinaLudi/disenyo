from gi.repository import Gtk

import psycopg2
import sys


class main:
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("/home/marina/Escritorio/Cargar_Pasajero.xml")
		
		self.window1 = builder.get_object("window1")
		self.button1 = builder.get_object("button1")
		self.entry1 = builder.get_object("entry1")
		#handlers = {
		#"on_button1_clicked": self.on_button1_clicked,
		#"on_window1_destroy": Gtk.main_quit
		#}
		#builder.connect_signals(handlers)
		self.window1.show_all()
class window:
	def __init___(self):
		Gtk.Window.__init__(self, title="Disenyo")

main()
Gtk.main()
