#!/usr/bin/python3

"""                                                                                                                                                                                                         
network statistics script:
    - print ip configuration              
    - print routing table
    - print network statistics
    - capture tcpdump traffic for 2 seconds
"""     

PASSWORD = "<ARG_NEXT_USER_PASSWORD>"

# Test running a process as another user
from subprocess import Popen, PIPE
p = Popen(["su", "-c", "whoami", "testuser"], stdin=PIPE, stdout=PIPE, stderr=PIPE)
out, err = p.communicate(b"testuser" + b"\n")
print(out.decode())

# Test running a process with sudo privileges
p = Popen(["sudo", "-l"], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
out, err = p.communicate(PASSWORD + "\n")
print(out.decode())
