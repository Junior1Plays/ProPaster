from colorama import Fore, Style, init
import configparser
import keyboard
import os
import time

config = configparser.ConfigParser()
config.read('configurações.ini')
delay_for_each_character = config.getfloat("configurations", "espera_a_cada_letra")
wait_time = config.getfloat("configurations", "tempo_de_espera")

init()

os.system("title ProPaster v1.0")

main_message = f'{Fore.GREEN}ProPaster v1.0\n{Fore.WHITE}feito por {Fore.MAGENTA}Junior Schueller{Style.RESET_ALL}'
print(main_message)

os.system('pause')

clipboard = ''''''

with open('texto.txt', 'r', encoding='utf-8') as file:
    clipboard = file.read()

time.sleep(wait_time)

keyboard.write(clipboard, delay=delay_for_each_character)
