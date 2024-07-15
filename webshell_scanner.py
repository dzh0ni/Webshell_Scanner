#!/usr/bin/env python3
#====================================================
#   SCRIPT:                   WEBSHELL SCANNER
#   DESARROLLADO POR:         JENN VALENTINE 
#   FECHA DE ACTUALIZACIÃ“N:  29-03-2024 
#   CONTACTO POR TELEGRAMA:   https://t.me/JennValentine
#   GITHUB OFICIAL:           https://github.com/JennValentine/Webshell_Scanner
#====================================================

# Importación de módulos necesarios
import argparse  # Para analizar los argumentos de la línea de comandos
import requests  # Para realizar solicitudes HTTP
import re  # Para trabajar con expresiones regulares
from urllib.parse import urljoin  # Para unir URL
from tqdm import tqdm  # Para mostrar una barra de progreso
from datetime import datetime  # Para obtener la fecha y hora actual
import sys  # Para manejar la interrupción de Ctrl + C

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

# Iconos v3
checkmark = f"{white}[{green}++{white}]{green}"
error = f"{white}[{red}--{white}]{reset}"
info = f"{white}[{yellow}**{white}]{white}"
unknown = f"{white}[{blue}!!{white}]{reset}"
process = f"{white}[{magenta}>>{white}]{magenta}"
indicator = f"{red}==>{reset}"

# Barra de separación
barra = f"{blue}|--------------------------------------------|{reset}"
bar = f"{yellow}{'-' * 45}{reset}"

# Función para verificar la existencia de una shell en una URL
def check_shell(url, shell):
    target_url = urljoin(url, shell)
    try:
        response = requests.head(target_url, allow_redirects=True)
        if response.status_code == 200:
            return target_url
    except requests.exceptions.RequestException:
        pass

# Función principal
def main():
    parser = argparse.ArgumentParser(description="Webshell Scanner")
    parser.add_argument("-u", "--url", help="URL del sitio web objetivo", required=True)
    parser.add_argument("-s", "--shell", help="Ruta del archivo que contiene la lista de nombres de shell", required=True)
    parser.add_argument("-d", "--directories", help="Ruta del archivo que contiene los directorios a escanear", default=None)
    parser.add_argument("-o", "--output", help="Guardar la salida en un archivo", metavar="output_file")
    args = parser.parse_args()

    # Mostrar información sobre la ejecución del script
    print(f"\n{bar}")
    print(f"{bold}WEBSHELL SCANNER v1.00{reset}")
    print(f"{bold}By JENN VALENTINE {reset}")
    print(f"{bar}\n")
    print(f"START_TIME: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")
    print(f"URL_BASE: {args.url}")
    print(f"WORDLIST_FILES: {args.shell}")
    if args.directories:
        print(f"DIRECTORIES_FILE: {args.directories}\n")
    else:
        print(f"DIRECTORIES_FILE: (No se proporcionó)\n")
    print(f"{bar}\n")

    found_shells = []  # Lista para almacenar las URL de las shells encontradas

    # Leer la lista de nombres de shell desde el archivo
    with open(args.shell, "r") as shell_file:
        shells = shell_file.read().splitlines()

    # Escaneo de las shells con una barra de progreso
    for shell in tqdm(shells, desc="Escaneando", unit="shells"):
        shell_path = check_shell(args.url, shell)
        if shell_path:
            found_shells.append(shell_path)
            print(f"{process} {white}{shell_path}{reset}")

    # Leer la lista de rutas guardadas en el archivo directorios_encontrados.txt
    if args.directories:
        with open(args.directories, "r") as dir_file:
            dirs = dir_file.read().splitlines()

        # Escaneo de las shells en los directorios
        for directory in dirs:
            dir_url = urljoin(args.url, directory)
            try:
                response = requests.get(dir_url)
                if response.status_code == 200:
                    dir_content = response.text
                    for shell in shells:
                        if shell in dir_content:
                            found_shells.append(urljoin(args.url, directory + "/" + shell))
                            print(f"{process} {white}{urljoin(args.url, directory + '/' + shell)}{reset}")
            except requests.exceptions.RequestException:
                pass

    # Mostrar la barra de separación nuevamente
    print(f"\n{bar}")

    # Mostrar las shells encontradas
    print(f"\n{bold}Shells encontradas:{reset}\n")
    for path in found_shells:
        path = re.sub(r'(http://[^/]+)/+', r'\1/', path)  # Reemplazar barras dobles después de http:// con una sola barra
        print(f"{green}{indicator} {path}{reset}")

    # Mostrar estadísticas finales
    print(f"\n{bold}Total de shells en base de datos:{reset} {len(shells)}")
    print(f"{bold}Shells encontradas:{reset} {len(found_shells)}")
    print(f"{bold}Shells no encontradas:{reset} {len(shells) - len(found_shells)}")

    print(f"\n{info} {white}GITHUB OFICIAL: {green}https://github.com/JennValentine/Webshell_Scanner{reset}")

    print(f"\n{bar}")

    # Guardar la salida en un archivo si se especifica la opción -o
    if args.output:
        with open(args.output, "w") as output_file:
            for path in found_shells:
                output_file.write(f"{path}\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{error} KeyboardInterrupt Operación cancelada. Saliendo del programa...")
        sys.exit(0)
