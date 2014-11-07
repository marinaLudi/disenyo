#### Gestor gestordb ####

from pipeline import Pipe

class GestorDB:
	# Guardamos un pasajero en la base de datos
	def guardarPasajero(usuario):
		pipeline = UserPipe()
		pipeline.process_item(usuario)

	# Buscamos un pasajero en la base de datos
	def buscarPasajero(nombre, apellido, tipoDocu, Documento):
		print ""
