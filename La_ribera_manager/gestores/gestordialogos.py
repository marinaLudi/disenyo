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
