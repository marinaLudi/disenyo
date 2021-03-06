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
from gestores.gestordialogos import GestorDialogos
from itertools import izip

# Globals
BORDE_ANCHO = 25
VENTANA_ALTO = 530
VENTANA_ANCHO = 735

class InterfazGestionarPasajero:
	def __init__(self,menu):
		self.menu = menu
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

		# Events handlers
		handlers = {
		"on_bSiguiente_clicked": self.on_bSiguiente_clicked,
		"on_bCancelar_clicked": self.on_bCancelar_clicked,
		"on_cDocumento_changed": self.on_cDocumento_changed,
		}
		builder.connect_signals(handlers)
		
		# Variable auxiliar
		self.tipo = None
		self.pasajero = None

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
		errores = gestionarPasajeros.correcto([{'nombre': nombre,
				'apellido': apellido,
				'codigo': codigo}],
			gestionarPasajeros.erroneo)
		
		if not errores:
            		arregloPasajeros = gestionarPasajeros.buscar(tipoDocu=self.tipo,
            				documento=codigo,
            				nombre=nombre,
            				apellido=apellido)



            		if not arregloPasajeros:
            			# Se genera la intefaz de dar alta pasajero
            			darAlta = InterfazDarAltaPasajero(self.menu)
            			self.window1.destroy()

            		else:
            			# Se muestra en la pantalla la grilla para seleccionar al pasajero
            			pasajero = self.seleccionarPasajero(arregloPasajeros)
            		
            	
            	else:
                    # Si se cometieron errores
                    dialogo = GestorDialogos()
                    dialogo.confirm(dialogo.crearAdvertencia(errores), "Aceptar")

                    # Obtenemos styles y widgets
                    widgets, styles = self.getEntries_Styles(errores)

                    # Despintamos todos los widgets
                    self.despintarWidgets([self.eNombre, self.eApellido, self.eDocumento],
                                    [self.eNombre.get_style_context(),
                                        self.eApellido.get_style_context(),
                                        self.eDocumento.get_style_context()])

                    # Pintamos widgets erroneos
                    self.pintarWidgets(widgets, styles)

	def on_bCancelar_clicked(self, boton):
		self.menu.show_all()
		self.window1.destroy()
		
	def pintarWidgets(self, widgets, styles):
		for widget, style in izip(reversed(widgets), reversed(styles)):
			style.add_class('invalid')
			widget.grab_focus()

	def despintarWidgets(self, widgets, styles):
		for widget, style in izip(reversed(widgets), reversed(styles)):
			style.remove_class('invalid')
			widget.grab_focus()

	def on_cDocumento_changed(self, combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.tipo = id_object
			
		

	def seleccionarPasajero(self,arregloPasajeros):
		self.window1.hide()
		builder = Gtk.Builder()
		
		
		builder.add_from_file("Lista_pasajeros.xml")
		window2 = builder.get_object("window2")
		lPasajeros = builder.get_object("lPasajeros")
		b2Siguiente = builder.get_object("b2Siguiente")
		treeView = builder.get_object("treeviewLista")

		
		window2.set_border_width(BORDE_ANCHO)
		window2.set_default_size(VENTANA_ANCHO, VENTANA_ALTO)
				
		for e in arregloPasajeros:
				lPasajeros.append([e.getNombre(),
					e.getApellido(),
					e.getDocumento().getTipo().getTipo(),
					e.getDocumento().getCodigo()])
		
		select = treeView.get_selection()
		select.unselect_all()
		
		select.connect("changed", self.on_tree_selection_changed)
		b2Siguiente.connect("clicked", self.on_b2Siguiente_clicked,window2,treeView)
		window2.show_all()
	
	def on_b2Siguiente_clicked(self,boton,window,treeView):
		if self.pasajero is None:
		# El usuario no elige ningun pasajero
			darAlta = InterfazDarAltaPasajero(self.menu)
			window.destroy()
	
	def on_tree_selection_changed(self,selection):
		model,treeiter = selection.get_selected()
		if treeiter != None:
			 self.pasajero = model[treeiter][0]
	
	def getEntries_Styles(self, omisiones):
		widgets = list()
		styles = list()

		# Agrupamos los widgets y los styles contexts
		for omision in omisiones:
			if omision is 'nombre':
				widgets.append(self.eNombre)
				styles.append(self.eNombre.get_style_context())
			
			elif omision is 'apellido':
				widgets.append(self.eApellido)
				styles.append(self.eApellido.get_style_context())

			elif omision is 'codigo':
				widgets.append(self.eDocumento)
				styles.append(self.eDocumento.get_style_context())

		# retornamos widgets y style contexts
		return widgets, styles
		

		
		
		

if __name__ == '__main__':		
	InterfazGestionarPasajero()
	Gtk.main()