#!/usr/bin/python
# -*- coding: utf-8 -*-

#### Interfaz Dar Alta Pasajero ####

import sys, os, inspect

# Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk, Gdk
import datetime
from objetos.dtopasajero import DtoPasajero
from gestores.gestorGestionarPasajeros import GestorGestionarPasajeros
from gestores.gestorcombos import GestorCombos
from gestores.gestordialogos import GestorDialogos
from itertools import izip

# Globals
BORDE_ANCHO = 25
VENTANA_ALTO = 530
VENTANA_ANCHO = 735

class InterfazDarAltaPasajero:
	def __init__(self,menu):
		
		self.menu = menu
		
		builder = Gtk.Builder()
		builder.add_from_file("Cargar_Pasajero3.4.xml")
		self.dialogo = GestorDialogos()
		
		
		#carga conecta los widgets con la interfaz
		self.window1 = builder.get_object("window1")
		self.bSiguiente = builder.get_object("bSiguiente")
		self.bCancelar = builder.get_object("bCancelar")
		self.eNombres = builder.get_object("eNombres")

		self.eApellidos = builder.get_object("eApellidos")
		self.eDocumento = builder.get_object("eDocumento")
		self.eTelefono = builder.get_object("eTelefono")
		self.eCalle = builder.get_object("eCalle")
		self.eNumero = builder.get_object("eNumero")
		self.eDepto = builder.get_object("eDepto")
		self.ePiso = builder.get_object("ePiso")
		self.ePostal = builder.get_object("ePostal")
		self.eCUIT = builder.get_object("eCUIT")
		self.cPais = builder.get_object("cPais")
		self.eCorreo = builder.get_object("eCorreo")

		self.cProvincia = builder.get_object("cProvincia")
		self.cLocalidad = builder.get_object("cLocalidad")
		self.cDocumento = builder.get_object("cDocumento")
		self.cDia = builder.get_object("cDia")
		self.cMes = builder.get_object("cMes")
		self.cAnyo = builder.get_object("cAnyo")
		self.cNacionalidad = builder.get_object("cNacionalidad")
		self.cOcupacion = builder.get_object("cOcupacion")

		self.lPais = builder.get_object("lPais")
		self.lNacionalidad = builder.get_object("lNacionalidad")
		self.lOcupacion = builder.get_object("lOcupacion")
		self.lProvincia = builder.get_object("lProvincia")
		self.lLocalidad = builder.get_object("lLocalidad")
		self.lDocumento = builder.get_object("lDocumento")
		self.lIVA = builder.get_object("lIVA")
		
		self.ebPais = builder.get_object("eventbox_pais")
		self.ebNacionalidad = builder.get_object("eventbox_nacionalidad")
		self.ebOcupacion = builder.get_object("eventbox_ocupacion")
		self.ebProvincia = builder.get_object("eventbox_provincia")
		self.ebLocalidad = builder.get_object("eventbox_localidad")
		self.ebDocumento = builder.get_object("eventbox_dni")
		self.ebIVA = builder.get_object("eventbox_iva")
		self.ebFecha = builder.get_object("eventbox_fecha")
		
		self.window1.set_border_width(BORDE_ANCHO)
		self.window1.set_default_size(VENTANA_ANCHO, VENTANA_ALTO)
	
		# Obtenemos informacion para los combos desde la db
		self.gestorCombos = GestorCombos()

		self.gestorCombos.cargarCombos(self.lPais,
				self.lNacionalidad,
				self.lOcupacion,
				self.lIVA,
				self.lDocumento)
				
		self.gestorCombos.initDateCombo(self.cDia,self.cMes,self.cAnyo,datetime.datetime.today().year-100,datetime.datetime.today().year)
		#variables auxiliares
		self.tipo = None
		self.localidad = None
		self.provincia = None
		self.nacionalidad = None
		self.pais = None
		self.ocupacion = None
		self.IVA = None
		self.fecha = datetime.date(0001,01,01)
		
		# CSS
		screen = Gdk.Screen.get_default()
		css_provider = Gtk.CssProvider()
		css_provider.load_from_path('style.css')
		priority = Gtk.STYLE_PROVIDER_PRIORITY_USER
		context = Gtk.StyleContext()
		context.add_provider_for_screen(screen, css_provider, priority)
		
		# Conecta las senales con sus funciones
		handlers = {
		"on_bSiguiente_clicked": self.on_bSiguiente_clicked,
		"on_bCancelar_clicked":self.on_bCancelar_clicked,
		"on_cPais_changed": self.on_cPais_changed,
		"on_cProvincia_changed": self.on_cProvincia_changed,
		"on_cLocalidad_changed": self.on_cLocalidad_changed,
		"on_cDocumento_changed": self.on_cDocumento_changed,
		"on_cNacionalidad_changed": self.on_cNacionalidad_changed,
		"on_cAnyo_changed": self.on_cAnyo_changed,
		"on_cMes_changed": self.on_cMes_changed,
		#"on_cDia_changed": self.on_cDia_changed,
		"on_cOcupacion_changed":self.on_cOcupacion_changed,
		"on_cIVA_changed":self.on_cIVA_changed
		}
		builder.connect_signals(handlers)
		
				
		# Mostramos ventanas con todos los widgets
		self.window1.show_all()
		
		
	def on_cDocumento_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.tipo = id_object
		
		
	def on_cOcupacion_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.ocupacion = id_object


	def on_cIVA_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.IVA = id_object
		

	def on_cNacionalidad_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.nacionalidad = id_object
	

	def on_cAnyo_changed(self,combo):
		self.gestorCombos.comboUpDate(self.cDia,self.cMes,self.cAnyo)
	
					
	def on_cMes_changed(self,combo):
		self.gestorCombos.comboUpDate(self.cDia,self.cMes,self.cAnyo)
	

	def on_cPais_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.pais = id_object
			self.gestorCombos.getProvincia(self.lProvincia,id_object)
		

	def on_cProvincia_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.provincia = id_object
			self.gestorCombos.getLocalidad(self.lLocalidad,id_object)
	

	def on_cLocalidad_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.localidad = id_object
	

	def on_bSiguiente_clicked(self,boton):
		pasajero = DtoPasajero(nombre=self.eNombres.get_text(),
				apellido=self.eApellidos.get_text(),
				cuit=self.eCUIT.get_text(),
				email=self.eCorreo.get_text(),
				fecha_de_nac=self.gestorCombos.getDate(self.cDia,self.cMes,self.cAnyo),
				telefono=self.eTelefono.get_text(),
				CP=self.ePostal.get_text(),
				id_iva=self.IVA,
				id_ocupacion=self.ocupacion,
				id_pais=self.pais,
				id_localidad=self.localidad,
				id_provincia=self.provincia,
				id_nacionalidad=self.nacionalidad,
				calle=self.eCalle.get_text(),
				numero=self.eNumero.get_text(),
				dpto=self.eDepto.get_text(),
				piso=self.ePiso.get_text(),
				id_tipo=self.tipo,
				codigo=self.eDocumento.get_text())
				

		gestor = GestorGestionarPasajeros()

		# Corroboramos que cada entry coincida con el formato de entrada
		errores, tipo = gestor.checkentries(pasajero)	

	
		
		if not errores:
		    	# creamos pasajero
		    	crear_return = gestor.crearPasajero(pasajero)	
			if crear_return == False:
				respuesta = self.dialogo.confirm("¡CUIDADO! El tipo y número de documento ya existen en el sistema", "Aceptar Igualmente", "Corregir")
				if respuesta == True:
					gestor.completarCarga(pasajero)

			elif crear_return == True:
				respuesta = self.dialogo.confirm('Pasajero Guardado',"Aceptar")
				self.menu.show_all()
				self.window1.hide()

		else:
			if tipo:
				# Si se cometieron errores
				# Obtenemos styles y widgets
				widgets, styles = self.getEntries_Styles(errores)
				
				# Pintamos widgets
				self.pintarWidgets(widgets, styles)
				
				# Monstramos errores
				self.dialogo.confirm(self.crearAdvertencia(errores),
						"Aceptar")

			else:
				# Si se realizaron omisiones
				# Obtenemos styles y widgets
				widgets, styles = self.getEntries_Styles(errores)
				
				self.despintarWidgets(self.getallwidgets(),self.getallstyles())
				# Pintamos widgets
				self.pintarWidgets(widgets, styles)
				
				
	def on_bCancelar_clicked(self,boton):
		
		respuesta = self.dialogo.confirm("¿Desea cancelar el alta del pasajero?","SI","NO")
		if respuesta == True:
			self.menu.show_all()
			self.window1.destroy()


	def getEntries_Styles(self, omisiones):
		widgets = list()
		styles = list()

		# Agrupamos los widgets y los styles contexts
		for omision in omisiones:
			if omision is 'nombre':
				widgets.append(self.eNombres)
				styles.append(self.eNombres.get_style_context())
			
			elif omision is 'apellido':
				widgets.append(self.eApellidos)
				styles.append(self.eApellidos.get_style_context())

			elif omision is 'id_tipo':
				widgets.append(self.ebDocumento)
				styles.append(self.ebDocumento.get_style_context())

			elif omision is 'codigo':
				widgets.append(self.eDocumento)
				styles.append(self.eDocumento.get_style_context())

			elif omision is 'id_nacionalidad':
				widgets.append(self.ebNacionalidad)
				styles.append(self.ebNacionalidad.get_style_context())

			elif omision is 'fecha':
				widgets.append(self.ebFecha)
				styles.append(self.ebFecha.get_style_context())

			elif omision is 'telefono':
				widgets.append(self.eTelefono)
				styles.append(self.eTelefono.get_style_context())

			elif omision is 'calle':
				widgets.append(self.eCalle)
				styles.append(self.eCalle.get_style_context())

			elif omision is 'numero':
				widgets.append(self.eNumero)
				styles.append(self.eNumero.get_style_context())

			elif omision is 'id_localidad':
				widgets.append(self.ebLocalidad)
				styles.append(self.ebLocalidad.get_style_context())

			elif omision is 'CP':
				widgets.append(self.ePostal)
				styles.append(self.ePostal.get_style_context())

			elif omision is 'id_provincia':
				widgets.append(self.ebProvincia)
				styles.append(self.ebProvincia.get_style_context())

			elif omision is 'id_pais':
				widgets.append(self.ebPais)
				styles.append(self.ebPais.get_style_context())

			elif omision is 'id_ocupacion':
				widgets.append(self.ebOcupacion)
				styles.append(self.ebOcupacion.get_style_context())

			elif omision is 'id_iva':
				widgets.append(self.ebIVA)
				styles.append(self.ebIVA.get_style_context())


		# retornamos widgets y style contexts
		return widgets, styles
		

	def pintarWidgets(self, widgets, styles):
		for widget, style in izip(reversed(widgets), reversed(styles)):
			style.add_class('invalid')
			widget.grab_focus()

		print "painting-finished"
	
	def despintarWidgets(self, widgets, styles):
		for widget, style in izip(reversed(widgets), reversed(styles)):
			style.remove_class('invalid')
			widget.grab_focus()


	def crearAdvertencia(self, errores):
		if len(errores) == 1:
			errorMessage = "Cometio un error al llenar el campo:"
		else:
			errorMessage = "Cometio un error al llenar los campos:"

		for error in errores:
			if error is 'nombre':
				errorMessage+= "\nNombre, debe tener la forma -> <nombre>{<espacio><segundonombre>}*"

			elif error is 'apellido':
				errorMessage+= "\nApellido, debe tener la forma -> <apellido>{<espacio><segundoapellido>}*"

			elif error is 'cuit':
				errorMessage+= "\nCUIT, debe tener la forma -> <tipo>-<codigo>-<digitoverificador>"

			elif error is 'email':
				errorMessage+= "\nEmail, debe tener la forma -> <usuario>@<host>.<dominio>"

			elif error is 'CP':
				errorMessage+= "\nCodigo Postal, debe tener como minimo 3 digitos y como maximo 9"

			elif error is 'dpto':
				errorMessage+= "\nDepartamento, debe ser una letra del alfabeto"

			elif error is 'piso':
				errorMessage+= "\nPiso, el piso min es 1 y el maximo 163"

		return errorMessage

	def getallstyles(self):
		return [self.eNombres.get_style_context(),
				self.eApellidos.get_style_context(),
				self.ebDocumento.get_style_context(),
				self.eDocumento.get_style_context(),
				self.ebNacionalidad.get_style_context(),
				self.ebFecha.get_style_context(),
				self.eTelefono.get_style_context(),
				self.eCalle.get_style_context(),
				self.eNumero.get_style_context(),
				self.ebLocalidad.get_style_context(),
				self.ePostal.get_style_context(),
				self.ebProvincia.get_style_context(),
				self.ebPais.get_style_context(),
				self.ebOcupacion.get_style_context(),
				self.ebIVA.get_style_context()]
	

	def getallwidgets(self):
		return [self.eNombres,
				self.eApellidos,
				self.ebDocumento,
				self.eDocumento,
				self.ebNacionalidad,
				self.ebFecha,
				self.eTelefono,
				self.eCalle,
				self.eNumero,
				self.ebLocalidad,
				self.ePostal,
				self.ebProvincia,
				self.ebPais,
				self.ebOcupacion,
				self.ebIVA]


		
if __name__ == '__main__':
	InterfazDarAltaPasajero()
	Gtk.main()
