#!/usr/bin/python3

USER = "<ARG_NEXT_USER_USERNAME>"
PASS = "L3TMEINFTPASSWORD123"

import ftplib
server = ftplib.FTP()
server.connect("bandit-18-server-ctr", 21)
server.login(USER, PASS)
print(server.dir())
