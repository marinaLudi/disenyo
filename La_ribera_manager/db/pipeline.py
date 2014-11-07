from sqlalchemy.orm import sessionmaker
from models import Pasajero, db_connect, create_pasajero_table

class PasajeroPipe(object):
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
PasajeroPipe()
