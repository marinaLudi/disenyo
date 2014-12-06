#### Gestor gestordb ####

from sqlalchemy.orm import sessionmaker
from models import db_connect, create_tables, Pasajero, Iva, Ocupacion, Pais, Nacionalidad, Documento, Provincia

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
		create_tables(engine)
		self.Session = sessionmaker(bind=engine)
		self.session = self.Session()

	def guardarObjeto(self, objeto):

		try:
			session.add(objeto)
			session.commit()

		except:
			session.rollback()

		finally:


		return objeto


	def buscarPasajero(self, nombre=None, apellido=None, tipoDocu=None, codigo=None):

		try:
			# Comienza la consulta
			query = session.query(Pasajero).join(Documento)
			
			# Dependiendo que valores se omitan en los parametros se decide que buscar
			# en la base de datos
			if nombre is not None:
				query = query.filter(Pasajero.nombre == nombre)

			if apellido is not None:
				query = query.filter(Pasajero.apellido == apellido)

			if codigo is not None:
				query = query.filter(Documento.codigo == codigo)

			if tipoDocu is not None:
				query = query.filter(Documento.id_tipo == tipoDocu)

			# Se completa la consulta
			arregloPasajeros = query.all()	

		except:
			raise

		finally:
	
	
		return arregloPasajeros


	def getObjs(self, tabla, ID):

		try:
			objeto = session.query(tabla).filter_by(**ID).all()

		except:
			raise
		
		finally:

		return objeto
		
	def getTabla(self,tabla):
		
		try:
			filas = session.query(tabla).all()
		except:
			session.rollback()
			raise
		finally:
					
		return filas
		
	def getTablaID(self, tabla, columna, ID):

		try:
			filas = session.query(tabla).filter(getattr(tabla, columna) == ID).all()
		except:
			raise
		finally:

		return filas
	
	def getObjetoID(self,objeto,ID):
		
		try:
			objeto = session.query(objeto).get(ID)
		except:
			raise
		finally:
			
		return objeto
		
