#### Menu Principal ####

from gi.repository import Gtk
from interfazGestionarPasajero import InterfazGestionarPasajero
from interfazOcuparHabitacion import InterfazOcuparHabitacion

# Globals
BORDE_ANCHO = 25
VENTANA_ALTO = 530
VENTANA_ANCHO = 735

class InterfazMenu:
	def __init__(self):
		builder = Gtk.Builder()

		# Dibuja ventanas desde .xml
		builder.add_from_file("menuprincipal.xml")

		# Obtenemos widgets
		self.window = builder.get_object("window")
		self.gestionar_pasajero_button = builder.get_object("gestionar_pasajero_button")
		self.ocupar_hab_button = builder.get_object("ocupar_hab_button")
		self.gestionar_rp_button = builder.get_object("gestionar_rp_button")
		self.ingresar_pago_button = builder.get_object("ingresar_pago_button")
		self.facturar_button = builder.get_object("facturar_button")
		self.ingresar_nc_button = builder.get_object("ingresar_nc_button")
		self.reservar_hab_button = builder.get_object("reservar_hab_button")
		self.gestionar_listados_button = builder.get_object("gestionar_listados_button")
		self.cambiar_usuario_button = builder.get_object("cambiar_usuario_button")

		# Configuramos tamano ventana
		self.window.set_border_width(BORDE_ANCHO)
		self.window.set_default_size(VENTANA_ANCHO, VENTANA_ALTO)

		# Event handlers
		handlers = {
		"onButtonPressed": self.buttonPressed,
		"onWindowDestroy": Gtk.main_quit
		}
		builder.connect_signals(handlers)

		# Monstramos ventana
		self.window.show_all()


	def buttonPressed(self, widget):
		if widget == self.gestionar_pasajero_button:
			gestionarPasajero = InterfazGestionarPasajero()
			self.window.hide()

		elif widget == self.ocupar_hab_button:
			ocuparHabitacion = InterfazOcuparHabitacion()
			self.window.hide()

		elif widget == self.gestionar_rp_button:
			print "gestionar_rp_button"

		elif widget == self.ingresar_pago_button:
			print "ingresar_pago_button"

		elif widget == self.facturar_button:
			print "facturar_button"

		elif widget == self.ingresar_nc_button:
			print "ingresar_nc_button"

		elif widget == self.reservar_hab_button:
			print "reservar_hab_button"

		elif widget == self.gestionar_listados_button:
			print "gestionar_listado_button"

		elif widget == self.cambiar_usuario_button:
			print "cambiar_usuario_button"



InterfazMenu()
Gtk.main()
