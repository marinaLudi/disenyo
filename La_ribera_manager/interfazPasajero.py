from gi.repository import Gtk
from sqlalchemy import *
import datetime
from objetos.dtopasajero import DtoPasajero

class interfazPasajero:
	def __init__(self):
		
		builder = Gtk.Builder()
		builder.add_from_file("interfaces/Cargar_Pasajero3.4.xml")
		
		self.window1 = builder.get_object("window1")
		self.bSiguiente = builder.get_object("bSiguiente")
		self.eNombres = builder.get_object("eNombres")
		self.eApellidos = builder.get_object("eApellidos")
		self.eDocumento = builder.get_object("eDocumento")
		self.eTelefono = builder.get_object("eTelefono")
		self.eDireccion = builder.get_object("eDireccion")
		self.eDepto = builder.get_object("eDepto")
		self.ePiso = builder.get_object("ePiso")
		self.ePostal = builder.get_object("ePostal")
		self.eCUIT = builder.get_object("eCUIT")
		self.eIVA = builder.get_object("eIVA")
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
		
		self.window1.set_border_width(25)
		self.cargarCombos(self.cPais,self.cProvincia,self.cLocalidad,self.cDocumento,self.cDia,self.cMes,self.cAnyo,self.cNacionalidad,self.cOcupacion,)
		
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
		"on_cOcupacion_changed":self.on_cOcupacion_changed
		}
		builder.connect_signals(handlers)
		
		self.window1.show_all()
		
	def on_cDocumento_changed(self,combo):
		print "sss"	
		
	def on_cOcupacion_changed(self,combo):
		print "sss"
		
	def on_cNacionalidad_changed(self,combo):
		print "sss"	
	
	def on_cAnyo_changed(self,combo):
		print "sss"	
	
	def on_cDia_changed(self,combo):
		print "sss"	
				
	def on_cLocalidad_changed(self,combo):
		print "sss"	
	
	def on_cMes_changed(self,combo):
		print "sss"	
		
	def on_bSiguiente_clicked(self,boton):#ver!
		pasajero = DtoPasajero(self.eNombres.get_text(),self.eApellidos.get_text(),self.eCUIT.get_text(),self.eCorreo.get_text(),None,self.eTelefono.get_text(),None,None,self.eDireccion.get_text(),self.eDepto.get_text(),self.ePiso.get_text(),self.ePostal.get_text(),self.eIVA.get_text())
		print pasajero.nombre
		
	def on_cPais_changed(self,combo):
		print "pais"
	def on_cProvincia_changed(self,combo):
		print "provincia"
	
	
	def cargarCombos(self,cPais,cProvincia,cLocalidad,cDocumento,cDia,cMes,cAnyo,cNacionalidad,cOcupacion):
		engine = create_engine('postgresql://marina:mari@localhost/marina')
		metadata = MetaData(engine)
		
		i = 1
		while i <= 31 :
			cDia.append_text(str(i))
			i = i+1
		
		meses = ['Enero','Febrero','Marzo','Abril','Mayo','Junio','Julio','Agosto','Septiembre','Octubre','Noviembre','Diciembre']
		for mes in meses:
			cMes.append_text(mes)
			
		ahora = datetime.datetime.now()
		anyoActual = ahora.year
		
		anyo = 1900
		while anyoActual >= anyo:
			cAnyo.append_text(str(anyoActual))
			anyoActual = anyoActual - 1
			
		pais = Table('pais',metadata,autoload=True)
		s = pais.select()
		rs = s.execute()
		fila = rs.fetchone()
		
		cPais.append_text(fila.nombre)
		for fila in rs:
			cPais.append_text(fila.nombre)
			
		provincia = Table('provincia',metadata,autoload=True)
		s = provincia.select()
		rs = s.execute()
		fila = rs.fetchone()
		
		cProvincia.append_text(fila.nombre)
		for fila in rs:
			cProvincia.append_text(fila.nombre)
			
		localidad = Table('localidad',metadata,autoload=True)
		s = localidad.select()
		rs = s.execute()
		fila = rs.fetchone()
		
		cLocalidad.append_text(fila.nombre)
		
		for fila in rs:
			cLocalidad.append_text(fila.nombre)	
			
		documento = Table('documento',metadata,autoload=True)
		s = documento.select()
		rs = s.execute()
		fila = rs.fetchone()
		
		cDocumento.append_text(fila.tipo)
		for fila in rs:
			cDocumento.append_text(fila.tipo)
			
		nacionalidad = Table('nacionalidad',metadata,autoload=True)
		s = nacionalidad.select()
		rs = s.execute()
		fila = rs.fetchone()
		
		cNacionalidad.append_text(fila.nombre)
		for fila in rs:
			cNacionalidad.append_text(fila.nombre)
			
		ocupacion = Table('ocupacion',metadata,autoload=True)
		s = ocupacion.select()
		rs = s.execute()
		fila = rs.fetchone()
		
		cOcupacion.append_text(fila.descripcion)
		for fila in rs:
			cOcupacion.append_text(fila.descripcion)
			 
			 

		
		
interfazPasajero()
Gtk.main()
