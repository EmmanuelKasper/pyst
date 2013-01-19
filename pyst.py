#!/usr/bin/env python
# -*- coding: utf8 -*-

# from the datetime module, import(?) the datetime class
from datetime import datetime
# from the subprocess module, import the call function
from subprocess import call
# from the sys module, get command line arguments in the current name context
from sys import argv

script, film = argv

my_time = datetime.now()
time_in_s = (my_time.hour * 3600) + (my_time.minute * 60) + my_time.second
vlc_cli = "cvlc --no-osd --fullscreen --loop --start-time" 
cmd_list = "%s %d %s" % (vlc_cli,time_in_s,film)
call (cmd_list, shell=True)

