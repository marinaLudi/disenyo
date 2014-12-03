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
			
	def cargarCombo(self,tabla):
		session = self.Session()
		try:
			tablas = session.query(tabla).all()
		except:
			session.rollback()
			raise
		finally:
			session.close()
			
		return tablas		
	
	def getProvincia(self, lProvincia, id_pais):
		session = self.Session()
		lProvincia.clear()
		provincias = session.query(Provincia.id_provincia,Provincia.nombreProv).filter(Provincia.id_pais == id_pais).all()
		for e in provincias:
			lProvincia.append([e.id_provincia,e.nombreProv])
		session.close()
		
	def getLocalidad(self, lLocalidad, id_provincia):
		session = self.Session()
		lLocalidad.clear()
		localidades = session.query(Localidad.id_localidad,Localidad.nombreLocalidad).filter(Localidad.id_provincia == id_provincia).all()
		for e in localidades:
			lLocalidad.append([e.id_localidad,e.nombreLocalidad])
		session.close()
		
			
	def instanciaObjetoID(self,objeto,ID):
		session = self.Session()
		objeto = session.query(objeto).get(ID)
		session.close()
		return objeto

