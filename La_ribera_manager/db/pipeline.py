from sqlalchemy.orm import sessionmaker
from models import db_connect, create_pasajero_table, Pais, Documento, Ocupacion, Nacionalidad,Provincia,Localidad,Iva

class Pipe(object):
	def __init__(self):
		"""
		Inicilializa la coneccion a la base de datos y el sessionmaker.
		construye tablas
		"""
		engine = db_connect()
		create_pasajero_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, objeto):
		session = self.Session()

		try:
			session.add(objeto)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()
					
		return objeto

	def getPasajeroList(self, nombre=None, apellido=None, tipoDocu=None, documento=None):
		session = self.Session()

		try:
			arregloPasajeros = session.query(Pasajero).filter(Pasajero.nombre == nombre, Pasajero.apellido == apellido, Pasajero.tipoDocu == tipoDocu, Pasajero.documento == documento).order_by(Pasajero.apellido).all()
		except:
			raise
		finally:
			session.close()

		return arregloPasajeros
		
	def cargarCombos(self,lPais,lNacionalidad,lOcupacion,lIVA):
		session = self.Session()
		
		paises = session.query(Pais.id_pais, Pais.nombrePais).all()
		for e in paises:
			lPais.append([e.id_pais, e.nombrePais])
		
		nacionalidades = session.query(Nacionalidad.id_nacionalidad,Nacionalidad.nombreNacionalidad).all()
		for e in nacionalidades:
			lNacionalidad.append([e.id_nacionalidad,e.nombreNacionalidad])
		
		ocupaciones = session.query(Ocupacion.id_ocupacion,Ocupacion.descripcion_ocupacion).all()
		for e in ocupaciones:
			lOcupacion.append([e.id_ocupacion,e.descripcion_ocupacion])
			
		ivas = session.query(Iva.id_iva,Iva.descripcion_iva).all()
		for e in ivas:
			lIVA.append([e.id_iva,e.descripcion_iva])
	
	def cargarDocumento(self, lDocumento):
		session = self.Session()
		documentos = session.query(Documento.codigo,Documento.tipo).all()
		for e in documentos:
			lDocumento.append([e.codigo,e.tipo])	
		
		
	
	def getProvincia(self, lProvincia, id_pais):
		session = self.Session()
		lProvincia.clear()
		provincias = session.query(Provincia.id_provincia,Provincia.nombreProv).filter(Provincia.id_pais == id_pais).all()
		for e in provincias:
			lProvincia.append([e.id_provincia,e.nombreProv])
		
	def getLocalidad(self, lLocalidad, id_provincia):
		session = self.Session()
		lLocalidad.clear()
		localidades = session.query(Localidad.id_localidad,Localidad.nombreLocalidad).filter(Localidad.id_provincia == id_provincia).all()
		for e in localidades:
			lLocalidad.append([e.id_localidad,e.nombreLocalidad])
		
			
