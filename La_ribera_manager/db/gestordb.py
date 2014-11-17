#### Gestor gestordb ####

from sqlalchemy.orm import sessionmaker
from models import db_connect, create_pasajero_table, Pasajero, Iva, Ocupacion, Pais, Nacionalidad

# Singleton como una metaclase
class Singleton(type):
	def __init__(cls, name, bases, dct):
		cls.__instance = None
		type.__init__(cls, name, bases, dct)

	def __call__(cls, *args, **kw):
		if cls.__instance is None:
			cls.__instance = type.__call__(cls, *args, **kw)

		return cls.__instance

class GestorDB:
	__metaclass__ = Singleton

	def __init__(self):
		"""
		Inicilializa la coneccion a la base de datos y el sessionmaker.
		construye tablas
		"""
		engine = db_connect()
		create_pasajero_table(engine)
		self.Session = sessionmaker(bind=engine)

	def guardarObjeto(self, objeto):
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

	def getObjectList(self, tabla, filtros, criterios):
		session = self.Session()

		try:
			arregloObjetos = session.query(tabla).filter_by(**filtros).order_by(*criterios).all()
		except:
			raise

		finally:
			session.close()

		return arregloObjetos


	def buscarPasajero(self, nombre, apellido, tipoDocu, documento):
		filtros = {'nombre':nombre, 'apellido':apellido, 
				'tipoDocu':tipoDocu, 'documento':documento}			

		return getObjectList(Pasajero, filtros, [pasajero.apellido])


	def getObjbyID(self, tabla, ID):
		session = self.Session()

		try:
			objeto = session.query(tabla).filter_by(**ID).first()

		except:
			raise
		
		finally:
			session.close()

		return objeto
