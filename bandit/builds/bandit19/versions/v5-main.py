#!/usr/bin/python3

"""                                                                                                                                                                                                         
network statistics script:
    - print ip configuration              
    - print routing table
    - print network statistics
    - capture tcpdump traffic for 2 seconds
"""     

from subprocess import Popen, PIPE

PASSWORD = "<ARG_NEXT_USER_PASSWORD>"

def capture_tcp_traffic():
    """
    Capture network traffic for 2 seconds and save to a file (capture.pcap)
    """

    pcap = Popen(["sudo", "timeout", "2", "tcpdump", "-w", "capture.pcap", "-i", "any", "-n"], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
    return pcap.communicate(PASSWORD + "\n")

capture_tcp_traffic()
