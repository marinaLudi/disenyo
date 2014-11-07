from sqlalchemy.orm import sessionmaker
from models import Pasajero, db_connect, create_pasajero_table

class Pipe(object):
	def __init__(self):
		"""
		Inicilializa la coneccion a la base de datos y el sessionmaker.
		crea la tabla pasajero
		"""
		engine = db_connect()
		create_pasajero_table(engine)
		self.Session = sessionmaker(bind=engine)

	def process_item(self, item):
		session = self.Session()
		pasajero = Pasajero(**item)

		try:
			session.add(pasajero)
			session.commit()
		except:
			session.rollback()
			raise
		finally:
			session.close()
		
		return item
	
	def getPasajeroList(self, nombre=None, apellido=None, tipoDocu=None, documento=None):
		session = self.Session()

		try:
			arregloPasajeros = session.query(Pasajero).filter(Pasajero.name == nombre, Pasajero.apellido == apellido, Pasajero.tipoDocu == tipoDocu, Pasajero.documento == documento).order_by(Pasajero.apellido)
		except:
			raise
		finally:
			session.close()

		return arregloPasajeros
