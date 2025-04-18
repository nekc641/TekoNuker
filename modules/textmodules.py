import os
import subprocess
import colorama
import time

def clear():
    if os.name == "nt":
        subprocess.Popen("cls", shell=True)
        time.sleep(0.1)
    else:
        print("\033c")
        time.sleep(0.1)

def menu():
    print (colorama.Fore.RED + """
                                    
  __            __    __                         ___                
 /\ \          /\ \__/\ \                      /'___\ __            
 \_\ \     __  \ \ ,_\ \ \____    ___   __  __/\ \__//\_\    ___    
 /'_` \  /'__`\ \ \ \/\ \ '__`\  / __`\/\ \/\ \ \ ,__\/\ \ /' _ `\  
/\ \L\ \/\ \L\.\_\ \ \_\ \ \L\ \/\ \L\ \ \ \_\ \ \ \_/\ \ \/\ \/\ \ 
\ \___,_\ \__/.\_\\ \__\\ \_,__/\ \____/\/`____ \ \_\  \ \_\ \_\ \_\
 \/__,_ /\/__/\/_/ \/__/ \/___/  \/___/  `/___/> \/_/   \/_/\/_/\/_/
                                            /\___/                  
                                            \/__/                   
""")
    print ("BY TEKO\n")

async def asynccprint(text, type):
    if type == 0:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.GREEN + "Success" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 1:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.RED + "Error" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 2:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.YELLOW + "Warn" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 3:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.RED + "Hazus" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)

def cprint(text, type):
    if type == 0:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.GREEN + "Success" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 1:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.RED + "Error" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 2:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.YELLOW + "Warn" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
    if type == 3:
        print (colorama.Fore.LIGHTBLACK_EX + "[" + colorama.Fore.RED + "Hazus" + colorama.Fore.LIGHTBLACK_EX + "] " + colorama.Fore.CYAN + text)
