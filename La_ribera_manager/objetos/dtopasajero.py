class dtoPasajero:
	def __init__(self, nombre=None, apellido=None, cuit=None, email=None, fecha_de_nac=None, telefono=None, tipo=None, codigo=None, numero=None, calle=None, dpto=None, piso=None, id_localidad=None, id_prov=None, id_pais=None, id_ocupacion=None, id_nacionalidad=None, id_iva=None, CP=None, nombreLocalidad=None,descripcion_ocupacion=None,nombrePais=None,nombreProv=None,nombreNacionalidad=None):

		# Atributos del objeto pasajero
		self.atributosPasajero = dict(nombre=nombre, apellido=apellido, cuit=cuit, email=email, fecha_de_nac=fecha_de_nac, telefono=telefono)

		# Atributos del objeto documento
		self.atributosDocumento = dict(tipo=tipo, codigo=codigo)
			
		# Atributos del objeto direccion, localidad, provincia y pais
		self.atributosDireccion = dict(calle=calle, numero=numero, dpto=dpto, piso=piso, CP=CP)
		self.atributosLocalidad = dict(id_localidad=id_localidad, nombreLocalidad=None)
		self.atributosProvincia = dict(id_provincia=id_prov, nombreProv=None)
		self.atributosPais = dict(id_pais=id_pais, nombrePais=None)

		#Atributos de ocupacion
		self.atributosOcupacion = dict(id_ocupacion=id_ocupacion, descripcion_ocupacion=None)
		self.atributosNacionalidad = dict(id_nacionalidad=id_nacionalidad,nombreNacionalidad=None)

		#Atributos de posicion frente al IVA
		self.atributosIva = dict(id_iva=id_iva, descripcion_iva=None)

		
	def pack(self):
		return [atributosPasajero, atributosDocumento,
				atributosDireccion, atributosLocalidad,
				atributosProvincia, atributosPais,
				atributosOcupacion, atributosNacionalidad,
				atributosIva]
					

