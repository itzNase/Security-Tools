
import socket
import time
import colorama
from colorama import Fore, Style, init
init()

print(Style.DIM + Fore.RED + (r"""
  __  __           _        ____          _   _                
 |  \/  | __ _  __| | ___  | __ ) _   _  | \ | | __ _ ___  ___ 
 | |\/| |/ _` |/ _` |/ _ \ |  _ \| | | | |  \| |/ _` / __|/ _ \
 | |  | | (_| | (_| |  __/ | |_) | |_| | | |\  | (_| \__ \  __/
 |_|  |_|\__,_|\__,_|\___| |____/ \__, | |_| \_|\__,_|___/\___|
                                  |___/                        """))

try:
    IP = input("Target IP: ")
    ports = [10, 443, 80, 8080]
    for port in ports:
        s = socket.socket()
        s.settimeout(5)
        result = s.connect_ex((IP, port))
        if result == 0:
            print(Style.BRIGHT + Fore.BLUE + f'PORT {port} is OPEN')
        else:
            print(Style.BRIGHT + Fore.RED + f'PORT {port} is CLOSED')




except(KeyError, LookupError, ConnectionRefusedError, ConnectionResetError, ConnectionError):
    print("Something went wrong.")
finally:
    print(Fore.WHITE + 'Operation Finished.' + Style.RESET_ALL)
    input("Press Enter to exit...")