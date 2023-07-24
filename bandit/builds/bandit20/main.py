#!/usr/bin/python3

"""
Network Statistics Tool Script. 
This performs the following functions:
    - ip interfaces
    - routing table
    - listening ports
    - established connections
    - network traffic for 2 seconds

Capturing network traffic was done without providing a password to sudo
"""

from subprocess import Popen, PIPE 
def get_ip_stats():
    """
    Return the IP interfaces using the 'ip a' command
    """

    ip = Popen(["ip", "a"], stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True)
    return ip.communicate()


def get_routing_table():
    """
    Return the routing table using the 'ip route' command
    """

    route = Popen(["ip", "route"], stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True)
    return route.communicate()


def get_listening_ports():
    """
    Return the listening ports using the 'ss -tuln' command
    """

    l_ports = Popen(["ss", "-tuln"], stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True)
    return l_ports.communicate()


def get_established_conns():
    """
    Return the established connections using the 'ss -plant | grep ESTAB' command
    """

    all_conns = Popen(["ss", "-plant"], stdin=PIPE, stderr=PIPE, stdout=PIPE, text=True)
    grep_estab_conns = Popen(["grep", "ESTAB"], stdin=all_conns.stdout, stdout=PIPE, stderr=PIPE, text=True)
    return grep_estab_conns.communicate()

def get_network_traffic():
    """
    Capture the network traffic for 2 seconds and save to capture.pcap.
    """

    pcap = Popen(["timeout", "2", "sudo", "tcpdump", "-w", "capture.pcap", "-i", "any", "-n"], stdin=PIPE, stdout=PIPE, stderr=PIPE, text=True)
    return pcap.communicate()


def get_option():
    """
    Return a valid option provided by a user.
    """

    options = ["IP configuration.", "Routing Table.", "Listening Ports.", "Established Connections.", "Network Traffic Capture."]
    while True:
        print("Network Statistics Tool. Select an option from below:")
        for idx, option in enumerate(options):
            print(f"{idx+1}. {option}")
        option = input("> Option: ")

        if int(option) not in range(1, len(options) + 1):
            print("\nInvalid option selected. Please select one of the options specified.\n")
            continue
        else:
            return option

def main():
    option = get_option()
    options_mapping = {
        "1": get_ip_stats,
        "2": get_routing_table,
        "3": get_listening_ports,
        "4": get_established_conns,
        "5": get_network_traffic
    }
    
    func = options_mapping[option]
    out, err = func()
    if err:
        print(err)
    else:
        print(out)


main()
