#!/usr/bin/env python
import sys
from gi.repository import Gtk

class StartupDialogHandler:

	def onExitStartupDialog(self, *args):
		Gtk.main_quit(*args)
		sys.exit()
