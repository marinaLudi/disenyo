import psycopg2
import sys

import pygtk
pygtk.require("2.0")

import gtk
import gtk.glade

class MainWin:
	def __init__(self):
		
		builder = gtk.Builder()
		builder.add_from_file("boton.xml")
		
		self.window1 = builder.get_object("window1")
		self.button1 = builder.get_object("button1")
		handlers = {
		"on_button1_clicked": self.on_button1_clicked,
		"on_window1_destroy": gtk.main_quit
		}
		builder.connect_signals(handlers)
		self.window1.show()

	def on_button1_clicked(self,widget):
		buscar()
		
 
def buscar():
	#Define our connection string
	conn_string = "host='localhost' dbname='marina' user='marina' password='mari'"
 
	# print the connection string we will use to connect
	print "Connecting to database\n	->%s" % (conn_string)
 
	# get a connection, if a connect cannot be made an exception will be raised here
	conn = psycopg2.connect(conn_string)
 
	# conn.cursor will return a cursor object, you can use this cursor to perform queries
	cursor = conn.cursor()
	print "Connected!\n"
	v="'juan'"
	cursor.execute("SELECT * from pasajero where quien = " + v)
	rows = cursor.fetchall()
	for row in rows:
		print "ID = ", row[0]
		"\n"
 
if __name__ == "__main__":
	MainWin()
	gtk.main()
	
