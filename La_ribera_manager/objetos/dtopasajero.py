class dtoPasajero:
	def __init__(self, nombre=None, apellido=None, cuit=None, email=None, fecha_de_nac=None, telefono=None, tipo=None, codigo=None, numero=None, calle=None, dpto=None, piso=None, id_localidad=None, id_provincia=None, id_pais=None, id_ocupacion=None, id_nacionalidad=None, id_iva=None, CP=None, nombreLocalidad=None,nombrePais=None,nombreProv=None,nombreNacionalidad=None):

		# Atributos del objeto pasajero
		self.atributosPasajero = dict(nombre=nombre, apellido=apellido, cuit=cuit, email=email, fecha_de_nac=fecha_de_nac, telefono=telefono)

		# Atributos del objeto documento
		self.atributosDocumento = dict(tipo=tipo, codigo=codigo)
			
		# Atributos del objeto direccion, localidad, provincia y pais
		self.atributosDireccion = dict(calle=calle, numero=numero, dpto=dpto, piso=piso, CP=CP)
		self.id_localidad=id_localidad
		self.id_provincia=id_provincia
		self.id_pais=id_pais

		#Atributos de ocupacion
		self.id_ocupacion = id_ocupacion
		self.id_nacionalidad=id_nacionalidad

		#Atributos de posicion frente al IVA
		self.id_iva = id_iva
		self.fecha_de_nac = fecha_de_nac

		
	def pack(self):
		return [atributosPasajero, atributosDocumento,
				atributosDireccion, atributosLocalidad,
				atributosProvincia, atributosPais,
				atributosOcupacion, atributosNacionalidad,
				atributosIva]
					

