#!/usr/bin/python3

import getpass
from subprocess import Popen, PIPE

"""
network statistics script:
    - print ip configuration
    - print routing table
    - print network statistics
    - capture tcpdump traffic for 2 seconds
"""

PASSWORD = getpass.getpass()

def get_option():
    option_selected = False
    while not option_selected:
        print("Network Statistics Tool. Select an option from below:")
        print("1. IP interfaces")
        print("2. Routing Table")
        print("3. Listening Ports")
        print("4. Established Connections")
        print("5. Network traffic for 3 seconds")
        option = input("> Option: ")

        if int(option) not in range(1, 6):
            print("\nInvalid option selected. Please select one of the options specified.\n")
        else:
            return option


def print_ip_information():
    p = Popen(["ip", "a"], stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True)
    out, err = p.communicate()
    print(out)


def print_route_table():
    p = Popen(["ip", "route"], stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True)
    out, err = p.communicate()
    print(out)


def print_ss_listening():
    p = Popen(["ss", "-tuln"], stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True)
    out, err = p.communicate()
    print(out)


def print_ss_established():
    ss = Popen(["ss", "-plant"], stdout=PIPE, text=True)
    grep = Popen(["grep", "ESTAB"], stdin=ss.stdout, stdout=PIPE)
    out, err = grep.communicate()
    print(out.decode())


def capture_tcp_traffic():
    p = Popen(["sudo", "timeout", "2", "tcpdump", "-w", "capture.pcap", "-i", "any", "-n"], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
    out, err = p.communicate(PASSWORD + "\n")
    print(out)

def main():
    option = get_option()
    if option == "1":
        print_ip_information()
    elif option == "2":
        print_route_table()
    elif option == "3":
        print_ss_listening()
    elif option == "4":
        print_ss_established()
    elif option == "5":
        capture_tcp_traffic()

main()
