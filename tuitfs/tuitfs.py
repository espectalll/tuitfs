#!/usr/bin/env python3
# coding: utf-8

import os, sys, yaml, twitter

try:
	if __name__ == "__main__" or "__main__.py":
		import gi
		gi.require_version('Gtk', '3.0')
		from gi.repository import Gtk
except ImportError as e:
	print(e)
	sys.exit(1)

try:
	settings_file = os.path.expanduser("~/.local/share/tuitdb.yaml")
	with open(settings_file, 'r') as f:
		settings = yaml.load(f)
except IOError as e:
	print(e)
	sys.exit(1)

def main():
	path = os.path.dirname(os.path.abspath(__file__)) + '/tuitfs'
	builder = Gtk.Builder()
	builder.add_from_file(path + '/ui.glade')

	window = builder.get_object('mainWindow')
	window.connect("delete-event", Gtk.main_quit)
	window.show_all()

	Gtk.main()

	sys.exit(0)

if __name__ == "__main__":
	main()
