#!/usr/bin/python3

from subprocess import Popen, PIPE
p = Popen(["su", "-c", "whoami", "testuser"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
out, err = p.communicate(b"testuser" + b"\n")
print(out)
