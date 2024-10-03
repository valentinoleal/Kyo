# Kyo-Ransomware

## Descripción

**Kyo-Ransomware** es un proyecto básico de ciberseguridad que tiene como objetivo mostrar cómo funcionan los conceptos de encriptación y desencriptación de archivos y directorios. El proyecto está diseñado para estudiantes o entusiastas de la ciberseguridad, y **no** debe utilizarse con fines malintencionados. Su uso está destinado a fines educativos y de prueba, en entornos controlados y con el consentimiento adecuado.

## Características

- **Encriptar archivos y directorios**: Utiliza un algoritmo de encriptación para asegurar el contenido.
- **Desencriptar archivos y directorios**: Proceso inverso que restaura los archivos a su estado original.
- **Menú interactivo**: Interfaz por consola que permite elegir entre las opciones de encriptación y desencriptación.
- **Soporte para múltiples directorios**: Puedes seleccionar uno o varios directorios para encriptar o desencriptar.
  
## Imagenes del proyecto:


## Instalación

1. Clona el repositorio en tu computadora:
    ```bash
    git clone https://github.com/valentinoleal/Kyo.git
    ```
2. Entra al directorio del proyecto:
    ```bash
    cd kyo/
    ```
3. Instala las dependencias:
    ```bash
    pip install -r requirements.txt
    ```

## Uso

1. Ejecuta el script principal para iniciar el programa:
    ```bash
    python main.py
    ```

2. Sigue las instrucciones en pantalla para elegir la opción deseada.


## Estructura del proyecto

```plaintext
kyo-ransomware/
│
├── main.py             # Archivo principal que ejecuta el menú
├── encriptar.py        # Módulo para encriptar archivos y directorios
├── desencriptar.py     # Módulo para desencriptar archivos y directorios
├── menu.py             # Módulo del menú interactivo
├── requirements.txt    # Librerías necesarias para ejecutar el proyecto
└── owner/              # Carpeta donde se guardan las claves de encriptación y la ruta de los objetivos seleccioandos