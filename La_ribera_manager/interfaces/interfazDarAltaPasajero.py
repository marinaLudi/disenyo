import sys, os, inspect

#Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk
import datetime
from objetos.dtopasajero import DtoPasajero
from gestores.gestorGestionarPasajeros import *
from gestores.gestorcombos import GestorCombos

# Globals
BORDE_ANCHO = 25
VENTANA_ANCHO = 530
VENTANA_ALTO = 735

class InterfazDarAltaPasajero:
	def __init__(self):
		
		builder = Gtk.Builder()
		builder.add_from_file("Cargar_Pasajero3.4.xml")
		
		
		#carga conecta los widgets con la interfaz
		self.window1 = builder.get_object("window1")
		self.bSiguiente = builder.get_object("bSiguiente")
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
		
		self.window1.set_border_width(BORDE_ANCHO)
		self.window1.set_default_size(VENTA_ALTO, VENTANA_ANCHO)
	
		# Obtenemos información para los combos desde la db
		self.gestorCombos = GestorCombos()

		self.gestorCombos.cargarCombos(self.lPais, 
				self.lNacionalidad,
				self.lOcupacion, 
				self.lIVA,
				self.lDocumento)
		
		#variables auxiliares
		self.tipo = None
		self.localidad = None
		self.provincia = None
		self.nacionalidad = None
		self.pais = None
		self.ocupacion = None
		self.IVA = None
		self.fecha = datetime.date(0001,01,01)
		
		
		
		#conecta las senyales con sus funciones
		handlers = {
		"on_bSiguiente_clicked": self.on_bSiguiente_clicked,
		"on_window1_destroy": Gtk.main_quit,
		"on_cPais_changed": self.on_cPais_changed,
		"on_cProvincia_changed": self.on_cProvincia_changed,
		"on_cLocalidad_changed": self.on_cLocalidad_changed,
		"on_cDocumento_changed": self.on_cDocumento_changed,
		"on_cNacionalidad_changed": self.on_cNacionalidad_changed,
		"on_cAnyo_changed": self.on_cAnyo_changed,
		"on_cMes_changed": self.on_cMes_changed,
		"on_cDia_changed": self.on_cDia_changed,
		"on_cOcupacion_changed":self.on_cOcupacion_changed,
		"on_cIVA_changed":self.on_cIVA_changed
		}
		builder.connect_signals(handlers)
		
				
		# Mostramos ventanas con todos los widgets
		self.window1.show_all()
		

	def cargarFechas(self,cDia,cMes,cAnyo):
			
		i = 1
		while i <= 31 :
			cDia.append_text(str(i))
			i = i+1
		
		i = 1
		while i <=12:
			cMes.append_text(str(i))
			i = i +1	
		
		
		ahora = datetime.datetime.now()
		anyoActual = ahora.year
		
		anyo = 1900
		while anyoActual >= anyo:
			cAnyo.append_text(str(anyoActual))
			anyoActual = anyoActual - 1
				
		
		
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
		self.fecha = self.fecha.replace(year=int(combo.get_active_text()))
	
	
	def on_cDia_changed(self,combo):
		self.fecha = self.fecha.replace(day=int(combo.get_active_text()))
	
					
	def on_cMes_changed(self,combo):
		self.fecha = self.fecha.replace(month=int(combo.get_active_text()))
	

	def on_cPais_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.pais = id_object
			self.gestorDireccion.getProvincia(self.lProvincia,id_object)
		

	def on_cProvincia_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.provincia = id_object
			self.gestorDireccion.getLocalidad(self.lLocalidad,id_object)
	

	def on_cLocalidad_changed(self,combo):
		treeIter = combo.get_active_iter()
		if treeIter != None:
			model = combo.get_model()
			id_object = model[treeIter][0]
			self.localidad = id_object
	

	def on_bSiguiente_clicked(self,boton):
		
		pasajero = DtoPasajero(nombre=self.eNombres.get_text(),
				apellido=self.eApellidos.get_text(), 
				email=self.eCorreo.get_text(), 
				fecha_de_nac=self.fecha, 
				telefono=self.eTelefono.get_text(), 
				CP=self.ePostal.get_text(), 
				id_iva=self.IVA, 
				id_ocupacion=self.ocupacion,
				id_pais=self.pais,
				id_localidad=self.localidad,
				id_prov=self.provincia,
				id_nacionalidad=self.nacionalidad,
				calle=self.eCalle.get_text(),
				numero=self.eNumero.get_text(),
				dpto=self.eDepto.get_text(),
				piso=self.ePiso.get_text(),
				tipo=self.tipo,
				codigo=self.eDocumento.get_text())

		gestor = GestorGestionarPasajeros()
		gestor.crearPasajero(pasajero)	
		 

		
		
interfazPasajero()
Gtk.main()
