#!/usr/bin/python
# -*- coding: utf-8 -*-

#### Interfaz Dar Alta Pasajero ####

import sys, os, inspect

# Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk,Gdk

class GestorDialogos:
	def confirm(self,pregunta,aceptar,cancelar=None):
		dialog = Gtk.MessageDialog(type=Gtk.MessageType.WARNING,message_format=pregunta)

		dialog.set_modal(True)

		dialog.add_button(aceptar, Gtk.ResponseType.YES)
		
		if cancelar is not None:
			dialog.add_button(cancelar, Gtk.ResponseType.NO)
			
		response = dialog.run()
		dialog.destroy()
		return response == Gtk.ResponseType.YES
	

	def presTecla(self,texto):
		dialog = Gtk.MessageDialog(message_format=texto)		
		dialog.set_modal(True)
		dialog.connect("key-press-event",self.on_dialog_key_press_event)
		response = dialog.run()
		dialog.destroy()	
		return response == Gtk.ResponseType.OK
	

	def on_dialog_key_press_event(self,dialog,event):
		dialog.response(Gtk.ResponseType.OK)
		

	def pregunta(self,pregunta,aceptar,cancelar=None,salir=None):
		dialog = Gtk.MessageDialog(type=Gtk.MessageType.QUESTION,message_format=pregunta)

		dialog.set_modal(True)

		dialog.add_button(aceptar, Gtk.ResponseType.YES)
		
		if cancelar is not None:
			dialog.add_button(cancelar, Gtk.ResponseType.NO)
		if salir is not None:
			dialog.add_button(salir,Gtk.ResponseType.CLOSE)
			
		response = dialog.run()
		dialog.destroy()
		return response


	def crearAdvertencia(self, errores):
		if len(errores) == 1:
			errorMessage = "Cometio un error al llenar el campo:"
		else:
			errorMessage = "Cometio un error al llenar los campos:"

		for error in errores:
			if error is 'nombre':
				errorMessage+= "\nNombre, debe tener la forma -> <nombre>{<espacio><segundonombre>}*"

			elif error is 'apellido':
				errorMessage+= "\nApellido, debe tener la forma -> <apellido>{<espacio><segundoapellido>}*"

			elif error is 'cuit':
				errorMessage+= "\nCUIT, debe tener la forma -> <tipo>-<codigo>-<digitoverificador>"

			elif error is 'email':
				errorMessage+= "\nEmail, debe tener la forma -> <usuario>@<host>.<dominio>"

			elif error is 'CP':
				errorMessage+= "\nCodigo Postal, debe tener como minimo 3 digitos y como maximo 9"

			elif error is 'dpto':
				errorMessage+= "\nDepartamento, debe ser una letra del alfabeto"

			elif error is 'piso':
				errorMessage+= "\nPiso, el piso min es 1 y el maximo 163"

		return errorMessage


		
