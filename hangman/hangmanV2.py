#including all libraries
import time
import os
from random import choice, randint, shuffle
from colorama import Fore, Back, Style

def welcome_screen():
  welcome_msg ="""
                   Welcome to 
   _                                             
  | |                                            
  | |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
  | '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
  | | | | (_| | | | | (_| | | | | | | (_| | | | |
  |_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                      __/ |                      
                     |___/
            by Dalaktronixs (c) 2023
                     """
  load_effect_symbol = "\u2588\u2588" # loading character
  loading_str = ""
  print(welcome_msg)
  time.sleep(3)
  os.system('clear')
  # Loading Effect for Initialization
  while True:
    for bar in range(0,101, 10):
      loading_str += load_effect_symbol
      print("******Initializing Game*******")
      print()
      print()
      print(Fore.RED + f"[ {loading_str} ]" + Fore.BLACK + Style.BRIGHT+ f" {bar} %")
      time.sleep(1)
      os.system("clear")
      
    print("Done Initializing")
    break

welcome_screen()