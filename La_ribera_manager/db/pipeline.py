from sqlalchemy.orm import sessionmaker
from models import db_connect, create_pasajero_table

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

	def getPasajeroList(self, filtros):
		session = self.Session()

		try:
			arregloPasajeros = session.query(Pasajero).filter(**filtros).order_by(Pasajero.apellido).all()
		except:
			raise
		finally:
			session.close()

		return arregloPasajeros
