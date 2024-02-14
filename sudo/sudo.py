import os
import sys
from colorama import Fore
def sudo():
 if os.geteuid() != 0:
    print(Fore.RED,"Please run this program with sudo.")
    sys.exit(1)
