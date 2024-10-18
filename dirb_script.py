#!/usr/bin/env python3
#====================================================
#   SCRIPT:                   Dirb Script- Webshell Scanner
#   DESARROLLADO POR:         Jenn Valentine 
#   FECHA DE ACTUALIZACIÓN:   29-03-2024 
#   CONTACTO POR TELEGRAMA:   https://t.me/JennValentine
#   GITHUB OFICIAL:           https://github.com/JennValentine/Webshell_Scanner
#====================================================

# Importación de módulos necesarios
import subprocess
import sys
import re
import time

# Paleta de colores
reset = "\033[0m"       # Restablecer todos los estilos y colores
bold = "\033[1m"        # Texto en negrita
italic = "\033[3m"      # Texto en cursiva
underline = "\033[4m"   # Texto subrayado
blink = "\033[5m"       # Texto parpadeante
reverse = "\033[7m"     # Invertir colores de fondo y texto
hidden = "\033[8m"      # Texto oculto (generalmente invisible)

# Colores de texto
black = "\033[0;30m"     # Negro
red = "\033[0;31m"       # Rojo
green = "\033[0;32m"     # Verde
yellow = "\033[0;33m"    # Amarillo
blue = "\033[0;34m"      # Azul
magenta = "\033[0;35m"   # Magenta
cyan = "\033[0;36m"      # Cian
white = "\033[0;37m"     # Blanco

# Colores de fondo
bg_black = "\033[0;40m"     # Fondo Negro
bg_red = "\033[0;41m"       # Fondo Rojo
bg_green = "\033[0;42m"     # Fondo Verde
bg_yellow = "\033[0;43m"    # Fondo Amarillo
bg_blue = "\033[0;44m"      # Fondo Azul
bg_magenta = "\033[0;45m"   # Fondo Magenta
bg_cyan = "\033[0;46m"      # Fondo Cian
bg_white = "\033[0;47m"     # Fondo Blanco

# Iconos
checkmark = f"{white}[{green}++{white}]{green}"
error = f"{white}[{red}--{white}]{reset}"
info = f"{white}[{yellow}**{white}]{white}"
unknown = f"{white}[{blue}!!{white}]{reset}"
process = f"{white}[{magenta}>>{white}]{magenta}"
indicator = f"{red}==>{reset}"

# Barra de separación
barra = f"{blue}|--------------------------------------------|{reset}"
bar = f"{yellow}{'-' * 45}{reset}"

def ejecutar_dirb(url):
    # Ejecutar Dirb y capturar la salida
    print(f"\n{process} {white}Ejecutando Dirb en {url}...")
    proceso = subprocess.Popen(['dirb', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = proceso.communicate()

    if proceso.returncode == 0:
        print(f"{checkmark} Dirb se ejecutó correctamente.\n")
        # Filtrar las líneas que contienen "DIRECTORY" o "CODE:200"
        directorios = [re.search(r'http://\S+', line).group() for line in stdout.split('\n') if '==> DIRECTORY:' in line]
        archivos = [re.search(r'http://\S+', line).group() for line in stdout.split('\n') if 'CODE:200' in line]
        return directorios, archivos
    else:
        print(f"{error} Error al ejecutar Dirb:")
        print(stderr)
        return [], []

def guardar_en_txt(datos, archivo):
    with open(archivo, 'w') as f:
        for dato in datos:
            # Quitar la barra final si existe
            dato = dato.rstrip('/')
            f.write(dato + '\n')
            print(f"{checkmark} Guardado en {archivo}: {dato}")
            time.sleep(0.1)  # Simulando un proceso de escritura más largo
    print(f"\n{info} Los datos han sido guardados en {archivo}\n")
    print(bar)

def manejador_interrupcion(signal, frame):
    print(f"\n\n{error} Interrupción de teclado. Operación cancelada. Saliendo del programa...")
    sys.exit(0)

if __name__ == "__main__":
    # Manejar la interrupción de teclado
    import signal
    signal.signal(signal.SIGINT, manejador_interrupcion)
    
    # Verificar la cantidad de argumentos
    if len(sys.argv) != 2:
        print(f"\n{info} {green}Uso: python3 dirb_script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    archivo_directorios = "directorios_encontrados.txt"
    archivo_archivos = "archivos_encontrados.txt"

    directorios_encontrados, archivos_encontrados = ejecutar_dirb(url)

    if directorios_encontrados:
        print(bar)
        print(f"\n{info} Directorios encontrados:\n")
        guardar_en_txt(directorios_encontrados, archivo_directorios)
    else:
        print(f"{error} No se encontraron directorios.")

    if archivos_encontrados:
        print(f"\n{info} Archivos encontrados:\n")
        guardar_en_txt(archivos_encontrados, archivo_archivos)
    else:
        print(f"{error} No se encontraron archivos.")
