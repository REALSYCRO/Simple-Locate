import json
import sys
from datetime import datetime
from colorama import Fore, init
init(convert=True)
import os
import requests
import time
import getpass
from console.utils import set_title
import easygui

debug = True

set_title(f"Simple Locate | by Sycro")

logo = f"""{Fore.RED}




                                                            
			_____ _           _        __                _   _         
			|   __|_|_____ ___| |___   |  |   ___ ___ ___| |_|_|___ ___ 
			|__   | |     | . | | -_|  |  |__| . |  _| .'|  _| | . |   |
			|_____|_|_|_|_|  _|_|___|  |_____|___|___|__,|_| |_|___|_|_|
						|_|                                           



				{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.RESET}{Fore.BLUE} Discord:{Fore.RESET} https://discord.gg/GnrnBPA9
				{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.RESET}{Fore.BLUE} GitHub:{Fore.RESET} REALSYCRO
				{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}]{Fore.RESET}{Fore.BLUE} GitHub Project:{Fore.RESET} https://github.com/REALSYCRO/Simple-Locate

                                                                                                                                                                                                        
{Fore.RESET}"""

url = "https://geolocation.onetrust.com/cookieconsentpub/v1/geo/location"

def banner():

	print(logo)

def locator():

	input("Press any Key to start...\n->")

	location = requests.get(url, 'r').json

	print(location)

	input()

class Main():

	banner()

	locator()


Main()
	