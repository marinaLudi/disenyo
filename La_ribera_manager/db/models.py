from sqlalchemy import create_engine, Column, Integer, String, Date, ForeignKey
from sqlalchemy.engine.url import URL
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship, backref

import settings

DeclarativeBase = declarative_base()

def db_connect():
	return create_engine(URL(**settings.DATABASE))

def create_pasajero_table(engine):
	DeclarativeBase.metadata.create_all(engine)


class TipoDocumento(DeclarativeBase):
	__tablename__ = "tipo_documento"

	# primary key
	id_tipo = Column(Integer, primary_key=True)

	# atributos
	tipo = Column(String, nullable=False)

	# gets 
	def getId(self):
		return self.id_tipo

	def getTipo(self):
		return str(self.tipo)

	# Devuelve una lista con los atributos
	def pack(self):
		return [self.getId(), self.getTipo()]


class Documento(DeclarativeBase):
	__tablename__ = "documento"

	# primary key
	id_documento = Column(Integer, primary_key=True)

	# atributos
	codigo = Column(String , nullable=False)
	
	# foreign keys
	id_tipo = Column(Integer, ForeignKey("tipo_documento.id_tipo"), nullable=False)

	# relacion
	tipo = relationship("TipoDocumento", backref=backref("documento", order_by=id_documento))

	# gets
	def getId(self):
		return self.id_documento

	def getCodigo(self):
		return str(self.codigo)

	def getTipo(self):
		return self.tipo

	# Pack
	def pack(self):
		return [self.getId(), self.getCodigo(), self.getTipo()]


class Iva(DeclarativeBase):
	__tablename__ = "iva"
	
	# primary key
	id_iva = Column(Integer, primary_key=True)

	# atributos
	descripcion_iva = Column("descripcion", String, nullable=False)

	# gets
	def getId(self):
		return self.id_iva

	def getDescripcion(self):
		return str(self.descripcion_iva)

	# Pack
	def pack(self):
		return [self.getId(), self.getDescripcion()]


class Ocupacion(DeclarativeBase):
	__tablename__ = "ocupacion"

	# primary key
	id_ocupacion = Column(Integer, primary_key=True)

	# atributos
	descripcion_ocupacion = Column("descripcion", String, nullable=False)

	# gets
	def getId(self):
		return self.id_ocupacion

	def getDescripcion(self):
		return str(self.descripcion_ocupacion)

	# Pack
	def pack(self):
		return [self.id_ocupacion, self.descripcion_ocupacion]


class Direccion(DeclarativeBase):
	__tablename__ = "direccion"

	# primary key
	id_direccion = Column(Integer, primary_key=True)

	# atributos
	calle = Column(String, nullable=False)
	numero = Column(Integer, nullable=False)
	dpto = Column(String)
	piso = Column(String)
	CP = Column(String, nullable=False)

	# foreign keys
	id_localidad = Column(Integer, ForeignKey("localidad.id_localidad"), nullable=False)
	
	#relacion
	localidad = relationship("Localidad",backref=backref("direccion",order_by=id_direccion))

	# gets
	def getId(self):
		return self.id_direccion

	def getCalle(self):
		return str(self.calle)

	def getNumero(self):
		return self.numero

	def getDpto(self):
		return str(self.dpto)

	def getPiso(self):
		return str(self.piso)

	def getCP(self):
		return str(self.CP)

	def getLocalidad(self):
		return self.localidad

	# pack
	def pack(self):
		return [self.getId(), 
				self.getCalle(), 
				self.getNumero(), 
				self.getDpto(), 
				self.getpiso(), 
				self.getCP(), 
				self.getLocalidad()]


class Localidad(DeclarativeBase):
	__tablename__ = "localidad"

	# primary key
	id_localidad = Column(Integer, primary_key=True)

	# atributos
	nombreLocalidad = Column("nombre", String, nullable=False)

	# foreign keys
	id_provincia = Column(Integer, ForeignKey("provincia.id_provincia"), nullable=False)
	
	# relacion
	provincia = relationship("Provincia",backref=backref("localidad",order_by=id_localidad))

	# gets
	def getId(self):
		return self.id_localidad

	def getNombre(self):
		return str(self.nombreLocalidad)

	def getProvincia(self):
		return self.provincia

	# pack
	def pack(self):
		return [self.getId(), self.getNombre(), self.getProvincia()]


class Provincia(DeclarativeBase):
	__tablename__ = "provincia"

	# primary key
	id_provincia = Column(Integer, primary_key=True)

	# atributos
	nombreProv = Column("nombre", String, nullable=False)

	# foreign keys
	id_pais = Column(Integer, ForeignKey("pais.id_pais"), nullable=False)

	#relacion
	pais = relationship("Pais",backref=backref("provincia",order_by=id_provincia))

	# gets
	def getId(self):
		return self.id_provincia

	def getNombre(self):
		return str(self.nombreProv)

	def getPais(self):
		return self.pais

	# pack
	def pack(self):
		return [self.getId(), self.getNombre(), self.getPais()]


class Pais(DeclarativeBase):
	__tablename__ = "pais"

	# primary key
	id_pais = Column(Integer, primary_key=True)

	# atributos
	nombrePais = Column("nombre", String, nullable=False)
	
	# gets
	def getId(self):
		return self.id_pais

	def getNombre(self):
		return str(self.nombrePais)

	# pack
	def pack(self):
		return [self.id_pais, self.nombrePais]


class Nacionalidad(DeclarativeBase):
	__tablename__ = "nacionalidad"
	
	#primary key
	id_nacionalidad = Column(Integer, primary_key=True)
	
	#atributos
	nombreNacionalidad = Column("nombre",String,nullable=False)

	# gets
	def getId(self):
		return self.id_nacionalidad

	def getNombre(self):
		return str(self.nombreNacionalidad)

	# pack
	def pack(self):
		return [self.id_nacionalidad, self.nombreNacionalidad]


class Pasajero(DeclarativeBase):
	__tablename__ = "pasajero"

	# primary key
	id_pasajero = Column(Integer, primary_key=True)

	# atributos
	nombre = Column(String, nullable=False)
	apellido = Column(String, nullable=False)
	cuit = Column(String, nullable=False)
	email = Column(String, nullable=False)
	fecha_de_nac = Column(Date, nullable=False)
	telefono = Column(String, nullable=False)

	# foreign keys
	id_documento = Column(Integer, ForeignKey("documento.id_documento"), nullable=False)
	id_direccion = Column(Integer, ForeignKey("direccion.id_direccion"), nullable=False)
	id_nacionalidad = Column(Integer, ForeignKey("nacionalidad.id_nacionalidad"), nullable=False)
	id_ocupacion = Column(Integer, ForeignKey("ocupacion.id_ocupacion"), nullable=False)
	id_iva = Column(Integer, ForeignKey("iva.id_iva"), nullable=False)

	#relacion
	documento = relationship("Documento",backref=backref("pasajero",order_by=id_pasajero))
	direccion = relationship("Direccion",backref=backref("pasajero",order_by=id_pasajero))	
	nacionalidad = relationship("Nacionalidad",backref=backref("pasajero",order_by=id_pasajero))
	ocupacion = relationship("Ocupacion",backref=backref("pasajero",order_by=id_pasajero))
	iva = relationship("Iva",backref=backref("pasajero",order_by=id_pasajero))

	# gets
	def getId(self):
		return id_pasajero

	def getNombre(self):
		return str(self.nombre)

	def getApellido(self):
		return str(self.apellido)

	def getCuit(self):
		return str(self.cuit)

	def getEmail(self):
		return str(self.email)

	def getFecha(self):
		return self.fecha_de_nac

	def getTelefono(self):
		return str(self.telefono)

	def getDocumento(self):
		return self.documento

	def getDireccion(self):
		return self.direccion

	def getNacionalidad(self):
		return self.nacionalidad

	def getOcupacion(self):
		return self.ocupacion

	def getIva(self):
		return self.iva

	# pack
	def pack(self):
		return [self.getId(), 
				self.getNombre(), 
				self.getApellido(), 
				self.getCuit(), 
				self.getEmail(), 
				self.getFecha(), 
				self.getTelefono(),
				self.getDocumento(), 
				self.getDireccion(), 
				self.getNacionalidad(), 
				self.getOcupacion(), 
				self.getIva()]

