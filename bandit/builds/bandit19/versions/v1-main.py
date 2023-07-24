#!/usr/bin/python3

from subprocess import Popen, PIPE
p = Popen(["whoami"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
out, err = p.communicate()
print(out)
