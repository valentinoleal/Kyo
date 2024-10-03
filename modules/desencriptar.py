<<<<<<< HEAD
from cryptography.fernet import Fernet,InvalidToken# type: ignore
import os
from colorama import Fore, init # type: ignore
import time
# Inicializa colorama para usar colores en la consola
init(autoreset=True)

# Definición de estilos de mensaje
advertencia = f"\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.WHITE}"
success = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}"
waiting = f"{Fore.WHITE}[{Fore.YELLOW}-{Fore.WHITE}] {Fore.WHITE}"
# Función para desencriptar un archivo
def desencriptar_archivo(ruta_archivo):
    base_dir = os.getcwd()
    owner_dir = os.path.join(base_dir, "owner")
    os.makedirs(owner_dir, exist_ok=True)

    # Ruta del archivo obj.txt dentro de la carpeta 'owner'
    objetivo_path = os.path.join(owner_dir, "obj.txt")

    try:
        # Lee la clave desde el archivo obj.txt
        with open(objetivo_path, 'r', encoding="UTF-8") as obj_file:
            ruta_completa = obj_file.read().strip()

        # Extrae el nombre del archivo desde la ruta completa
        nombre_archivo = os.path.basename(ruta_completa)

        # Ruta completa del archivo de clave en la carpeta 'owner'
        key_path = os.path.join(owner_dir, f"{nombre_archivo}.txt")

        # Abre el archivo que contiene la clave
        with open(key_path, 'rb') as key_file:
            key = key_file.read()

        # Crea una instancia de Fernet con la clave
        fernet = Fernet(key)

        # Verifica si el archivo existe antes de intentar abrirlo
        if not os.path.exists(ruta_archivo):
            print(f"El archivo {ruta_archivo} no existe.")
            return

        # Abre el archivo a desencriptar
        with open(ruta_archivo, 'rb') as file:
            data = file.read()

        # Desencripta el contenido
        decrypted_data = fernet.decrypt(data)

        # Sobrescribe el archivo con los datos desencriptados
        with open(ruta_archivo, 'wb') as file:
            file.write(decrypted_data)
        nombre_archivo = os.path.basename(ruta_archivo)
        print(f"{success}{nombre_archivo} fue desencriptado correctamente!")

    except FileNotFoundError:
        print(f"El archivo de clave o el archivo de entrada no se encontró.")
    except InvalidToken:
        print(f"Error: La clave es incorrecta o el archivo está corrupto.")
    except Exception as e:
        print(f"Error durante la desencriptación: {str(e)}")


# Función para desencriptar todos los archivos en un directorio
def desencriptar_directorio(directorio):
    # Crea la carpeta 'owner' si no existe
    base_dir = os.getcwd()
    owner_dir = os.path.join(base_dir, "owner")
    os.makedirs(owner_dir, exist_ok=True)

    # Ruta del archivo obj.txt dentro de la carpeta 'owner'
    objetivo_path = os.path.join(owner_dir, "obj.txt")

    try:
        # Lee la ruta del directorio desde el archivo obj.txt
        with open(objetivo_path, 'r', encoding="UTF-8") as obj_file:
            ruta_completa = obj_file.read().strip()

        # Extrae el nombre del archivo desde la ruta completa
        nombre_archivo = os.path.basename(ruta_completa)

        # Ruta completa del archivo de clave en la carpeta 'owner'
        key_path = os.path.join(owner_dir, f"{nombre_archivo}.txt")

        # Abre el archivo que contiene la clave
        with open(key_path, 'rb') as key_file:
            key = key_file.read()

        # Crea una instancia de Fernet con la clave
        fernet = Fernet(key)

        print(f"{Fore.CYAN}CTRL + C para cancelar la acción...")
        time.sleep(2)
        print(f"\n{Fore.LIGHTRED_EX}------------------------------ LOGS DESENCRIPTACIÓN ------------------------------\n")

        # Recorre el directorio y desencripta archivos
        for root, _, archivos in os.walk(directorio):
            for archivo in archivos:
                if archivo:  # Verifica que el archivo no esté vacío
                    ruta_completa = os.path.join(root, archivo)  # Genera la ruta completa del archivo
                    print(f"{waiting}Desencriptando archivo: {ruta_completa}")
                    desencriptar_archivo(ruta_completa)  # Solo pasa la ruta del archivo

    except Exception as e:
        print(f"{advertencia}Error durante la desencriptación: {str(e)}")
=======
from cryptography.fernet import Fernet,InvalidToken# type: ignore
import os
from colorama import Fore, init # type: ignore
import time
# Inicializa colorama para usar colores en la consola
init(autoreset=True)

# Definición de estilos de mensaje
advertencia = f"\n\n{Fore.WHITE}[{Fore.YELLOW}!{Fore.WHITE}] {Fore.WHITE}"
success = f"{Fore.WHITE}[{Fore.GREEN}+{Fore.WHITE}] {Fore.WHITE}"
waiting = f"{Fore.WHITE}[{Fore.YELLOW}-{Fore.WHITE}] {Fore.WHITE}"
# Función para desencriptar un archivo
def desencriptar_archivo(ruta_archivo):
    base_dir = os.getcwd()
    owner_dir = os.path.join(base_dir, "owner")
    os.makedirs(owner_dir, exist_ok=True)

    # Ruta del archivo obj.txt dentro de la carpeta 'owner'
    objetivo_path = os.path.join(owner_dir, "obj.txt")

    try:
        # Lee la clave desde el archivo obj.txt
        with open(objetivo_path, 'r', encoding="UTF-8") as obj_file:
            ruta_completa = obj_file.read().strip()

        # Extrae el nombre del archivo desde la ruta completa
        nombre_archivo = os.path.basename(ruta_completa)

        # Ruta completa del archivo de clave en la carpeta 'owner'
        key_path = os.path.join(owner_dir, f"{nombre_archivo}.txt")

        # Abre el archivo que contiene la clave
        with open(key_path, 'rb') as key_file:
            key = key_file.read()

        # Crea una instancia de Fernet con la clave
        fernet = Fernet(key)

        # Verifica si el archivo existe antes de intentar abrirlo
        if not os.path.exists(ruta_archivo):
            print(f"El archivo {ruta_archivo} no existe.")
            return

        # Abre el archivo a desencriptar
        with open(ruta_archivo, 'rb') as file:
            data = file.read()

        # Desencripta el contenido
        decrypted_data = fernet.decrypt(data)

        # Sobrescribe el archivo con los datos desencriptados
        with open(ruta_archivo, 'wb') as file:
            file.write(decrypted_data)
        nombre_archivo = os.path.basename(ruta_archivo)
        print(f"{success}{nombre_archivo} fue desencriptado correctamente!")

    except FileNotFoundError:
        print(f"El archivo de clave o el archivo de entrada no se encontró.")
    except InvalidToken:
        print(f"Error: La clave es incorrecta o el archivo está corrupto.")
    except Exception as e:
        print(f"Error durante la desencriptación: {str(e)}")


# Función para desencriptar todos los archivos en un directorio
def desencriptar_directorio(directorio):
    # Crea la carpeta 'owner' si no existe
    base_dir = os.getcwd()
    owner_dir = os.path.join(base_dir, "owner")
    os.makedirs(owner_dir, exist_ok=True)

    # Ruta del archivo obj.txt dentro de la carpeta 'owner'
    objetivo_path = os.path.join(owner_dir, "obj.txt")

    try:
        # Lee la ruta del directorio desde el archivo obj.txt
        with open(objetivo_path, 'r', encoding="UTF-8") as obj_file:
            ruta_completa = obj_file.read().strip()

        # Extrae el nombre del archivo desde la ruta completa
        nombre_archivo = os.path.basename(ruta_completa)

        # Ruta completa del archivo de clave en la carpeta 'owner'
        key_path = os.path.join(owner_dir, f"{nombre_archivo}.txt")

        # Abre el archivo que contiene la clave
        with open(key_path, 'rb') as key_file:
            key = key_file.read()

        # Crea una instancia de Fernet con la clave
        fernet = Fernet(key)

        print(f"{Fore.CYAN}CTRL + C para cancelar la acción...")
        time.sleep(2)
        print(f"\n{Fore.LIGHTRED_EX}------------------------------ LOGS DESENCRIPTACIÓN ------------------------------\n")

        # Recorre el directorio y desencripta archivos
        for root, _, archivos in os.walk(directorio):
            for archivo in archivos:
                if archivo:  # Verifica que el archivo no esté vacío
                    ruta_completa = os.path.join(root, archivo)  # Genera la ruta completa del archivo
                    print(f"{waiting}Desencriptando archivo: {ruta_completa}")
                    desencriptar_archivo(ruta_completa)  # Solo pasa la ruta del archivo

    except Exception as e:
        print(f"{advertencia}Error durante la desencriptación: {str(e)}")
>>>>>>> 50d7d16cfe24721f70808753e33f4cc7d70e4f11
