#!/usr/bin/python
# -*- coding: utf-8 -*-

#### Interfaz Dar Alta Pasajero ####

import sys, os, inspect

# Agregamos directorio padre al path
currentdir = os.path.dirname(os.path.abspath(inspect.getfile(inspect.currentframe())))
parentdir = os.path.dirname(currentdir)
sys.path.insert(0, parentdir)

from gi.repository import Gtk

class GestorDialogos:
	def confirm(widget,aceptar,cancelar, pregunta):
		dialog = Gtk.MessageDialog(type=Gtk.MessageType.WARNING,message_format=pregunta)

		dialog.set_modal(True)

		dialog.add_button(aceptar, Gtk.ResponseType.YES)
		dialog.add_button(cancelar, Gtk.ResponseType.NO)
			
		response = dialog.run()
		dialog.destroy()
		return response == Gtk.ResponseType.YES
