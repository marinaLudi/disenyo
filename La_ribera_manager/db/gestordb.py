#### Gestor gestordb ####

from pipeline import Pipe

class GestorDB:
	# Guardamos un pasajero en la base de datos
	def guardarPasajero(self,usuario):
		pipeline = Pipe()
		pipeline.process_item(usuario)
		print "ejecuta guardar Pasajero"

	# Buscamos un pasajero en la base de datos
	def buscarPasajero(nombre, apellido, tipoDocu, Documento):
		print ""
