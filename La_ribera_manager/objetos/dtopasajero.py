class dtoPasajero:
	def __init__(self, nombre=None, apellido=None, cuit=None, email=None, fecha_de_nac=None, telefono=None, tipo=None, codigo=None, numero=None, calle=None, piso=None, dpto=None, piso=None, id_localidad=None, id_prov=None, id_pais=None, id_ocupacion=None, id_nacionalidad=None, id_iva=None):

		# Atributos del objeto pasajero
		atributosPasajero = dict(nombre=nombre, apellido=apellido, cuit=cuit, email=email, fecha_de_nac=fecha_de_nac, telefono_telefono)
		
		# Atributos del objeto documento
		atributosDocumento = dict(tipo=tipo, codigo=codigo)
			
		# Atributos del objeto direccion, localidad, provincia y pais
		atributosDireccion = dict(calle=calle, numero=numero, dpto=dpto, piso=piso, CP=CP)
		atributosLocalidad = dict(id_localidad=id_localidad, nombreLocalidad=None)
		atributosProvincia = dict(id_provincia=id_prov, nombreProv=None)
		atributosPais = dict(id_pais=id_pais, nombrePais=None)

		#Atributos de ocupacion
		atributosOcupacion = dict(id_ocupacion=id_ocupacion, descripcion_ocupacion=None)

		#Atributos de posicino frente al IVA
		atributosIva = dict(id_iva=id_iva, descripcion_iva=None)




