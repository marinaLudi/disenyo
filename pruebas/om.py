#!/usr/bin/python3

from gi.repository import Gtk

import psycopg2
import sys


class main:
	def __init__(self):
		builder = Gtk.Builder()
		builder.add_from_file("entrada.xml")
		
		self.window1 = builder.get_object("window1")
		self.button1 = builder.get_object("button1")
		self.entry1 = builder.get_object("entry1")
		handlers = {
		"on_button1_clicked": self.on_button1_clicked,
		"on_window1_destroy": Gtk.main_quit
		}
		builder.connect_signals(handlers)
		self.window1.show_all()



	def on_button1_clicked(self,widget):
		texto = self.entry1.get_text()
		buscar(texto)

def buscar(texto):
	#Define our connection string
	conn_string = "host='localhost' dbname='marina' user='marina' password='mari'"
 
	# print the connection string we will use to connect
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	v=str(texto)
	cursor.execute("SELECT * from pasajero where quien = " + v)
	rows = cursor.fetchall()
		
main()
Gtk.main()
