<<<<<<< HEAD

from modules import menu as bfw_menu_pakage
from colorama import Fore, init# type: ignore
import os


os.system('cls' if os.name == 'nt' else 'clear')


init(autoreset=True)  #Reiniciar el estilo después de cada print

bfw_menu_pakage.mostrar_menu()

success = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}"
advertencia = f"\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.WHITE}"
=======

from modules import menu as bfw_menu_pakage
from colorama import Fore, init# type: ignore
import os


os.system('cls' if os.name == 'nt' else 'clear')


init(autoreset=True)  #Reiniciar el estilo después de cada print

bfw_menu_pakage.mostrar_menu()

success = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}"
advertencia = f"\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.WHITE}"
>>>>>>> 50d7d16cfe24721f70808753e33f4cc7d70e4f11
