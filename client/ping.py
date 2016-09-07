


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



def check(ping_url, network_interface, server_url):
    """
    Tries to ping the ping_url, i.e www.google.com, - if that succeds, makes a GET request to server(server_url) to store this machines IP address.
    If ping fails, then bring down, bring up network_interface, i.e wlan0, and finally run dhclient for network_interfae.
    """

    import os
    import httplib2
    
    if ping(ping_url):
        print "ping.py: pinging " + ping_url + " suceeded."
        ip_addr = get_ip_address(network_interface) #get our ip
        
        print "ping.py: ip address is: " + ip_addr
        req, content = httplib2.Http().request(server_url+ip_addr)
        
        print "ping.py: response from server: " + content
        return True
        #make GET rew
    else:
        print "ping.py: ping failed. will try to bring wlan0 down and up."
        try:
            os.system("ifdown " + network_interface)
            os.system("ifup " + network_interface)
            os.system("dhclient " + network_interface)
            print "ping.py: ifup, ifdown and dhclient run succesfully on " + network_interface
            return True
        except Exception:
            print "ping.py: ifup, ifdown, dhclient failed on " + network_interface
            return False



#start process def start
ping_google = "www.google.se"
net_interface = "wlan0"
server_address= "http://46.101.252.64:5000/setip/"
if check(ping_google, net_interface, server_address):
    print "ping.py: ping " + ping_google + " ok. IP is " + get_ip_address(net_interface) + ". " + server_address + " requested."
else:
    print "nope"
