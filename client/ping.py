


def ping(host):
    """
    returns True if host responds to ping request
    """


    import os, platform

    #Ping parameters as function of OS
    ping_str = "-n 1" if platform.system().lower()=="windows" else "-c 1"

    #Do the ping
    return os.system("ping " + ping_str + " " + host) == 0




def get_ip_address(ifname):
    """
    returns the IP for the provided (parameter) network interface.
    the SIOCFIG address only tested on  RPi infrastructure.
    """
    
    import socket
    import fcntl
    import struct
    try:
        s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        return socket.inet_ntoa(fcntl.ioctl(s.fileno(), 0x8915,  # SIOCGIFADDR
                                        struct.pack('256s', ifname[:15])
                                    )[20:24])
    except Exception:
        return False



def check():
    """
    Tries to ping google - if that succeds, makes a GET request to server to store this machines IP address.
    If ping fails, then bring down, bring up wlan0 and finally run dhclient for wlan0.
    """

    import os
    import requests
    
    if ping("www.google.se"):
        print "ping.py: pinging google suceeded."
        ip_addr = get_ip_address("wlan0") #get our ip
        r = requests.get("http://46.101.252.64:5000/setip/"+ip_addr)
        print "ping.py: response from server: " + r.content
        return True
        #make GET rew
    else:
        print "ping.py: ping failed. will try to bring wlan0 down and up."
        try:
            os.system("ifdown wlan0")
            os.system("ifup wlan0")
            os.system("dhclient wlan0")
            return True
        except Exception:
            print "ping.py: shell commands failed"
            return False



"""
if get_ip_address("wlan0"):
    print get_ip_address("wlan0")
else:
    print "nope"

"""


if check():
    print get_ip_address("wlan0")
else:
    print "nope"
