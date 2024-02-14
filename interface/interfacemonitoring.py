from colorama import Fore
from time import sleep
import os
def interface(interface):
   
        print(Fore.YELLOW,f'Monitoring {interface}')
        os.system(f'sudo airmon-ng start {interface}')
        print(Fore.WHITE,f'successful monitoring {interface}')
        print(Fore.CYAN,'---------------------------------------------------------------------------')


