


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
  if ping("www.google.se"):
      print "hooray"
  else:
      print "nope"





if get_ip_address("wlan0"):
    print get_ip_address("wlan0")
else:
    print "nope"
