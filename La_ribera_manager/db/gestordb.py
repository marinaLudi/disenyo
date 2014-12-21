#### Gestor gestordb ####

from sqlalchemy.orm import sessionmaker, contains_eager
from sqlalchemy import or_
from models import *
import datetime

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

	#~ try:
		self.session.add(objeto)
		self.session.commit()

	#~ except:
		self.session.rollback()


		return objeto


	def buscarPasajero(self, nombre=None, apellido=None, tipoDocu=None, codigo=None):

		try:
			# Comienza la consulta
			query = self.session.query(Pasajero).\
			join(Documento).\
			options(contains_eager(Pasajero.documento))
			
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

		return arregloPasajeros


	def getObjs(self, tabla, **ID):

		try:
			objeto = self.session.query(tabla).filter_by(**ID).all()
		except:
			raise

		return objeto
		

	def getTabla(self,tabla):	
		try:
			filas = self.session.query(tabla).all()
		except:
			self.session.rollback()
			raise

		return filas
		

	def getTablaID(self, tabla, columna, ID):

		try:
			filas = self.session.query(tabla).filter(getattr(tabla, columna) == ID).all()
		except:
			raise


		return filas
	

	def getObjetoID(self, objeto, ID):
		
		try:
			objeto = self.session.query(objeto).get(ID)
		except:
			raise

		return objeto
	
	def getEstado(self,tabla,fecha,hab):
		try:
			arregloTablas = self.session.query(tabla).filter(tabla.nro_habitacion==hab).filter(tabla.fecha_inicio <= fecha, tabla.fecha_fin >= fecha).all()
		except:
			raise	
		return arregloTablas



	def getHab(self):
		try:
			arregloHabitaciones = self.session.query(Habitacion).order_by(Habitacion.id_tipo). \
			all()

		except:
			raise

		return arregloHabitaciones
	
	
	def buscarHospedado(self,id_pasajero,fecha_ini, fecha_fin):
	    estadia = self.session.query(Estadia).join("ocupantes",tiene_ocupante).join(Pasajero).filter(Estadia.fecha_inicio<=fecha_ini,fecha_ini<=Estadia.fecha_fin).filter(Pasajero.id_pasajero==id_pasajero)
	    estadia2 = self.session.query(Estadia).filter(Estadia.fecha_inicio<=fecha_fin,fecha_fin<=Estadia.fecha_fin).filter(Pasajero.id_pasajero==id_pasajero)
	    estadia3 = self.session.query(Estadia).filter(Estadia.fecha_inicio>fecha_ini,Estadia.fecha_fin<fecha_fin).filter(Pasajero.id_pasajero==id_pasajero)
	    estadiaParcial = estadia.union(estadia2)
	    estadiaFinal = estadiaParcial.union(estadia3).all()
	    return estadiaFinal
	        #.filter(or_(Estadia.fecha_inicio<=fecha_ini,
	       #  Estadia.fecha_fin>=fecha_fin )).all()
	        #filter(tiene_ocupante.id_pasajero==id_pasajero,).
