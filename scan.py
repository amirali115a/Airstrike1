from scapy.all import *
from threading import Thread
import pandas
import time
import os
import argparse
from colorama import Fore
import argparse
print (Fore.GREEN,'''
   .               .    
 .´  ·  .     .  ·  `.  Sharknet 2.6.0
 :  :  :  (¯)  :  :  :  a tool for  scanning wifi 
 `.  ·  ` /¯\ ´  ·  .´  
   `     /¯¯¯\     ´    https://github.com/amirali115a/Sharknet

                                    
''')

parser = argparse.ArgumentParser(description="A python script for sending deauthentication frames")
parser.add_argument("-i", dest="iface", help="Interface to use, must be in monitor mode, default is 'wlan0mon'", default="wlan0mon")
args = parser.parse_args()
iface = args.iface
os.system('neofetch')
1



networks = pandas.DataFrame(columns=["BSSID", "SSID", "dBm_Signal", "Channel", "Crypto"])
networks.set_index("BSSID", inplace=True)

def callback(packet):
    if packet.haslayer(Dot11Beacon):
    
        bssid = packet[Dot11].addr2
       
        ssid = packet[Dot11Elt].info.decode()
        try:
            dbm_signal = packet.dBm_AntSignal
        except:
            dbm_signal = "N/A"
       
        stats = packet[Dot11Beacon].network_stats()
       
        channel = stats.get("channel")
        
        crypto = stats.get("crypto")
        networks.loc[bssid] = (ssid, dbm_signal, channel, crypto)


def print_all():
    while True:
        os.system('clear')
        print(networks)
        time.sleep(0.5)


def change_channel():
    ch = 1
    while True:
        os.system(f"iwconfig {iface} channel {ch}")
        
        ch = ch % 14 + 1
        time.sleep(0.5)


if __name__ == "__main__":
   

    
    print (Fore.GREEN,'''
   .               .    
 .´  ·  .     .  ·  `.  Sharknet 2.6.0
 :  :  :  (¯)  :  :  :  a tool for  scanning wifi 
 `.  ·  ` /¯\ ´  ·  .´  
   `     /¯¯¯\     ´    https://github.com/amirali115a/Sharknet

                                    
''')


    printer = Thread(target=print_all)
    printer.daemon = True
    printer.start()
   
    channel_changer = Thread(target=change_channel)
    channel_changer.daemon = True
    channel_changer.start()
 
    sniff(prn=callback, iface=iface)



