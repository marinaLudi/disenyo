from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base

import settingsm

DeclarativeBase = declarative_base()

def db_connect():
	return create_engine(URL(**settingsm.DATABASE))

def create_pasajero_table(engine):
	DeclarativeBase.metadata.create_all(engine)

class Pasajero(DeclarativeBase):
	__tablename__ = "pasajero"

	id_pasajero = Column(Integer, primary_key=True)
	nombre = Column('nombre', String, nullable=False)
	apellido = Column('apellido', String, nullable=False)
	cuit = Column('cuit', String, nullable=False)
	email = Column('email', String, nullable=False)
#	fecha_de_nac = Column('fecha_de_nac', Date, nullable=False)
	telefono = Column('telefono', String, nullable=False)

	"""#foreign keys
	codigo = Column('codigo', Integer, ForeignKey("documento.codigo"), nullable=False)
	id_direccion = Column('id_direccion', Integer, ForeignKey("direccion.id_direccion"), nullable=False)
	id_nacionalidad = Column('id_nacionalidad', Integer, ForeignKey("nacionalidad.id_nacionalidad"), nullable=False)
	id_ocupacion = Column('id_ocupacion', Integer, ForeignKey("ocupacion.id_ocupacion"), nullable=False)
	id_iva = Column('id_iva', Integer, ForeignKey("posicion_iva.id_iva"), nullable=False)
"""

