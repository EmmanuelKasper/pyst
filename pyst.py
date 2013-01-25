#!/usr/bin/env python
# -*- coding: utf8 -*-

# from the datetime module, import(?) the datetime class
from datetime import datetime
# from the subprocess module, import the call function
from subprocess import call
# from the sys module, get command line arguments in the current name context
from sys import argv,exit

script, film = argv

while 1:

	now = datetime.now()
	time_in_s = (now.hour * 3600) + (now.minute * 60) + now.second

	vlc_cli = "cvlc --no-osd --fullscreen --play-and-exit --start-time" 
	cmd_list = "%s %d %s" % (vlc_cli,time_in_s,film)

	call (cmd_list, shell=True)

sys.exit(0)



