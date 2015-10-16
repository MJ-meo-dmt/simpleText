#!/usr/bin/env python
# gitdoc (*temp name)
import os, sys
from git import Repo, GitCommandError
from gi.repository import Gtk

join = os.path.join
repo = Repo("testRepo/repo/")
assert not repo.bare

currentFile = "doc.txt"

def handleGit():
	#print repo.git.status()
	try:
		repo.git.add(currentFile)
		commitInfo = repo.git.commit(m="update File")
		pushInfo = repo.git.push()

	except GitCommandError, command:
		if command:
			info = repo.git.status()
			statusBar.push(0, info[-42:])

def save(_arg):
	textBuffer = builder.get_object("textbuffer1")

	start = textBuffer.get_start_iter()
	end = textBuffer.get_end_iter()

	text = textBuffer.get_text(start, end, True)

	f = open('testRepo/repo/doc.txt', 'w')
	f.write(text)
	f.close()

	# Now push and save it
	handleGit()

def firstRun():
	#pullInfo = repo.git.pull()
	#statusBar.push(0, pullInfo)

	f = open('testRepo/repo/doc.txt', 'r+')
	text = f.read()
	textBuffer = builder.get_object("textbuffer1")
	textBuffer.set_text(text)
	f.close()


def quit(*args):
	Gtk.main_quit(*args)
	sys.exit()

def handleGitSettings(*args):
	gitSettingsDialog = builder.get_object("dialog1")
	gitSettingsDialog.show_all()


class Handler:
    def onDeleteWindow(self, *args):
        Gtk.main_quit(*args)
        sys.exit()

builder = Gtk.Builder()
builder.add_from_file("layout.glade")
builder.add_from_file("git_settings_layout.glade")
builder.connect_signals(Handler())

window = builder.get_object("window1")
window.show_all()

savebtn = builder.get_object("imagemenuitem3")
savebtn.connect("activate", save)

quitbtn = builder.get_object("imagemenuitem5")
quitbtn.connect("activate", quit)

gitSettings = builder.get_object("gitSettings")
gitSettings.connect("activate", handleGitSettings)

statusBar = builder.get_object("statusbar1")


firstRun()
Gtk.main()
