#!/usr/bin/env python

import pygtk
pygtk.require('2.0')
import gtk
import hashlib

IMAGE_PATH = "/home/argot/images/celestine_avatar.png"
ICON_PATH = "/home/argot/images/logo.png"
ENTRY_MAX = 15

class LoginWin:
	"""A login window"""
	# Delete callback
	def delete_event(self, widget, event, data=None):
		print "Goodbye! :^)"
		gtk.main_quit()
		return False

	# Checking password callback
	def checking(self, widget, data=None):
		print "Checking user -> %s...\n" % data[0]
		checkpass(data[0], data[1])	

	def __init__(self):
		# Creates window and set title
		window = gtk.Window(gtk.WINDOW_TOPLEVEL)
		window.set_title("LOGIN")
		window.set_icon_from_file(ICON_PATH)
		
		window.connect("delete_event", self.delete_event)

		window.set_border_width(10)

		# We create a vertical box to pack widgets into
		outterbox = gtk.VBox(False, 10)
		outterbox.show()
		window.add(outterbox)

		# We create buttons and images to fill the outterbox
		# Image
		image = gtk.Image()
		image.set_from_file(IMAGE_PATH)

		outterbox.pack_start(image, False, False, 30)
		image.show()

		# Textbox1
		textbox1 = gtk.Entry(ENTRY_MAX)
		textbox1.set_text("Usuario")
		textbox1.select_region(0, len(textbox1.get_text()))

		outterbox.pack_start(textbox1, False, False, 20)
		textbox1.show()

		# Textbox2
		textbox2 = gtk.Entry(ENTRY_MAX)
		textbox2.set_visibility(False)

		outterbox.pack_start(textbox2, False, False, 20)
		textbox2.show()
		
		# At last we show the window
		window.show()

	def main(self):
		gtk.main()
		return 0

if __name__ == "__main__":
	pr = LoginWin()
	pr.main()
