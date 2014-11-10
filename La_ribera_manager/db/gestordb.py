#### Gestor gestordb ####

from pipeline import Pipe

class GestorDB:
	def __init__(self):
		pipeline = Pipe()
	# Guardamos un pasajero en la base de datos
	def guardarPasajero(objeto):
		return pipeline.process_item(objeto)

	# Buscamos un pasajero en la base de datos
	def buscarPasajero(filtros):
		return pipeline.getPasajeroList(filtros)
