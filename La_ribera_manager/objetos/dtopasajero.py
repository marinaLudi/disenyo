class DtoPasajero:
	def __init__(self, nombre=None, apellido=None, cuit=None,
			email=None, fecha_de_nac=None, telefono=None,
			codigo=None, id_tipo=None, numero=None,
			calle=None, dpto=None, piso=None,
			id_localidad=None, id_prov=None, id_pais=None,
			id_ocupacion=None, id_nacionalidad=None, id_iva=None,
			CP=None):

		# Atributos del objeto pasajero
		self.atributosPasajero = dict(nombre=nombre, apellido=apellido, cuit=cuit,
				email=email, fecha_de_nac=fecha_de_nac, telefono=telefono)

		# Atributos del objeto documento
		self.codigo = codigo 
		self.id_tipo = id_tipo
			
		# Atributos del objeto direccion, localidad, provincia y pais
		self.atributosDireccion = dict(calle=calle, numero=numero, dpto=dpto, piso=piso, CP=CP)
		self.id_localidad=id_localidad
		self.id_provincia=id_prov
		self.id_pais=id_pais

		#Atributos de ocupacion y nacionalidad
		self.id_ocupacion = id_ocupacion
		self.id_nacionalidad=id_nacionalidad

		#Atributos de posicion frente al IVA
		self.id_iva = id_iva

	# sets 
	def setNombre(self, nombre):
		self.atributosPasajero['nombre'] = nombre

	def setApellido(self, apellido):
		self.atributosPasajero['apellido'] = apellido

	def setCuit(self, cuit):
		self.atributosPasajero['cuit'] = cuit
	
	def setEmail(self, email):
		self.atributosPasajero['email'] = email
	
	def setFechaNac(self, fecha):
		self.atributosPasajero['fecha_de_nac'] = fecha

	def setTelefono(self, telefono):
		self.atributosPasajero['telefono'] = telefono
		
	def setCodigo(self, codigo_documento):
		self.codigo = codigo_documento

	def setIdTipo(self, id_tipo):
		self.id_tipo = id_tipo

	def setCalle(self, calle):
		self.atributosDireccion['calle'] = calle

	def setNumero(self, numero):
		self.atributosDireccion['numero'] = numero

	def setDpto(self, dpto):
		self.atributosDireccion['dpto'] = dpto

	def setPiso(self, piso):
		self.atributosDireccion['piso'] = piso

	def setCP(self, CP):
		self.atributosDireccion['CP'] = CP

	def setIdLocalidad(self, id_localidad):
		self.id_localidad = id_localidad

	def setIdProvincia(self, id_provincia):
		self.id_provincia = id_provincia

	def setIdPais(self, id_pais):
		self.id_pais = id_pais

	def setIdOcupacion(self, id_ocupacion):
		self.id_ocupacion = id_ocupacion

	def setIdNacionalidad(self, id_nacionalidad):
		self.id_nacionalidad = id_nacionalidad

	def setIdIva(self, id_iva):
		self.id_iva = id_iva

	# gets
	def getNombre(self):
		return self.atributosPasajero['nombre']	

	def getApellido(self):
		return self.atributosPasajero['apellido'] 

	def getCuit(self):
		return self.atributosPasajero['cuit']
	
	def getEmail(self):
		return self.atributosPasajero['email'] 
	
	def getFechaNac(self):
		return self.atributosPasajero['fecha_de_nac']

	def getTelefono(self):
		return self.atributosPasajero['telefono']
		
	def getCodigo(self):
		return self.codigo

	def getIdTipo(self):
		return self.id_tipo

	def getCalle(self):
		return self.atributosDireccion['calle']

	def getNumero(self):
		return self.atributosDireccion['numero']

	def getDpto(self, dpto):
		return self.atributosDireccion['dpto']

	def getPiso(self, piso):
		return self.atributosDireccion['piso']

	def getCP(self, CP):
		return self.atributosDireccion['CP']

	def getIdLocalidad(self):
		return self.id_localidad

	def getIdProvincia(self):
		return self.id_provincia

	def getIdPais(self):
		return self.id_pais

	def getIdOcupacion(self):
		return self.id_ocupacion

	def getIdNacionalidad(self):
		return self.id_nacionalidad

	def getIdIva(self):
		return self.id_iva

	def getAtributosPasajero(self):
		return self.atributosPasajero

	def getAtributosDireccion(self):
		return self.atributosDireccion


	def pack(self):
		return [self.getAtributosPasajero(), 
				self.getAtributosDireccion(),
				self.getIdLocalidad(), 
				self.getIdProvincia(),
				self.getIdPais(), 
				self.getIdOcupacion(),
				self.getIdNacionalidad(), 
				self.getIdIva()]

