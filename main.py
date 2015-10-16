#!/usr/bin/env python

import os
import sys

from git import Repo, GitCommandError
from gi.repository import Gtk

from config import ConfigHandler
from startupHandler import StartupDialogHandler

#-----------------------------------------------------#
# Main App
#-----------------------------------------------------#
class Main():

	def __init__(self):

		# Start up
		# Check for config file
		try: 
			ConfigHandler.readCfg()

		except:
			print "Missing Config File, write new file!"
			ConfigHandler.writeCfg()

		# Set the builder (is it wise to only use one?)
		self.builder = Gtk.Builder()

		# Load Glades
		self.loadGladeFiles()
		
		# Call startup
		self.callStartupDialog()

		# Start Gtk
		Gtk.main()

	def loadGladeFiles(self):
		self.builder.add_from_file("startup_dialog.glade")
		self.builder.connect_signals(StartupDialogHandler())

	def callStartupDialog(self):
		self.startupDialog = self.builder.get_object("dialog1")
		self.startupDialog.show_all()

	def callMainWindow(self):
		pass


m = Main()

