#!/usr/bin/env python3
#====================================================
#   SCRIPT:                   Escáner de Webshells
#   DESARROLLADO POR:         Jenn Valentine 
#   ÚLTIMA ACTUALIZACIÓN:     29-03-2024 
#   CONTACTO VIA TELEGRAM:    https://t.me/JennValentine
#   GITHUB OFICIAL:           https://github.com/JennValentine/Webshell_Scanner
#====================================================

#====================================================
#    Modificado por: Lance Kenji
#    Github: https://github.com/lancekenji
#    Contacto: https://t.me/lance_aswwscxzc
#====================================================

#====================================================
# v1 - Traducción al Español | Implementación de Hilos usando `concurrent`
#====================================================

# Importar módulos necesarios
import argparse  # Para analizar argumentos de la línea de comandos
import requests  # Para hacer solicitudes HTTP
import re  # Para trabajar con expresiones regulares
from urllib.parse import urljoin  # Para unir URLs
from tqdm import tqdm  # Para mostrar una barra de progreso
from datetime import datetime  # Para obtener la fecha y hora actuales
import sys  # Para manejar la interrupción Ctrl + C
from concurrent.futures import ThreadPoolExecutor, as_completed  # Para threading

# Paleta de colores
reset = "\033[0m"       # Restablecer todos los estilos y colores
bold = "\033[1m"        # Texto en negrita
italic = "\033[3m"      # Texto en cursiva
underline = "\033[4m"   # Texto subrayado
blink = "\033[5m"       # Texto parpadeante
reverse = "\033[7m"     # Colores invertidos
hidden = "\033[8m"      # Texto oculto (típicamente invisible)

# Colores de texto
black = "\033[0;30m"    # Negro
red = "\033[0;31m"      # Rojo
green = "\033[0;32m"    # Verde
yellow = "\033[0;33m"   # Amarillo
blue = "\033[0;34m"     # Azul
magenta = "\033[0;35m"  # Magenta
cyan = "\033[0;36m"     # Cian
white = "\033[0;37m"    # Blanco

# Colores de fondo
bg_black = "\033[0;40m"    # Fondo negro
bg_red = "\033[0;41m"      # Fondo rojo
bg_green = "\033[0;42m"    # Fondo verde
bg_yellow = "\033[0;43m"   # Fondo amarillo
bg_blue = "\033[0;44m"     # Fondo azul
bg_magenta = "\033[0;45m"  # Fondo magenta
bg_cyan = "\033[0;46m"     # Fondo cian
bg_white = "\033[0;47m"    # Fondo blanco

# Iconos
checkmark = f"{white}[{green}++{white}]{green}"
error = f"{white}[{red}--{white}]{reset}"
info = f"{white}[{yellow}**{white}]{white}"
unknown = f"{white}[{blue}!!{white}]{reset}"
process = f"{white}[{magenta}>>{white}]{magenta}"
indicator = f"{red}==>{reset}"

# Separadores
separator = f"{blue}|{'-' * 44}|{reset}"
bar = f"{yellow}{'-' * 45}{reset}"

# Función para verificar si existe un shell en una URL
def check_shell(base_url, shell_name):
    target_url = urljoin(base_url, shell_name)
    try:
        response = requests.head(target_url, allow_redirects=True)
        if response.status_code == 200:
            return target_url
    except requests.RequestException:
        pass
    return None

# Función para escanear directorios en busca de shells
def scan_directories(base_url, directories, shells):
    found_shells = []
    for directory in directories:
        dir_url = urljoin(base_url, directory)
        try:
            response = requests.get(dir_url)
            if response.status_code == 200:
                content = response.text
                for shell in shells:
                    if shell in content:
                        shell_url = urljoin(base_url, directory + "/" + shell)
                        found_shells.append(shell_url)
        except requests.RequestException:
            pass
    return found_shells

# Función principal
def main():
    # Analizar argumentos de la línea de comandos
    parser = argparse.ArgumentParser(description="Escáner de Webshells")
    parser.add_argument("-u", "--url", help="URL del sitio web objetivo", required=True)
    parser.add_argument("-s", "--shell", help="Archivo que contiene los nombres de los shells", required=True)
    parser.add_argument("-d", "--directories", help="Archivo que contiene directorios para escanear", default=None)
    parser.add_argument("-t", "--threads", help="Hilos (por defecto: 10)", default=10)
    parser.add_argument("-o", "--output", help="Guardar salida en un archivo", metavar="output_file")
    args = parser.parse_args()

    # Imprimir información del script
    print(f"\n{bar}")
    print(f"{bold}ESCÁNER DE WEBSHELLS v1.00{reset}")
    print(f"{bold}Por JENN VALENTINE{reset}")
    print(f"{bar}\n")
    print(f"HORA_INICIO: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")
    print(f"URL_BASE: {args.url}")
    print(f"ARCHIVO_LISTA_SHELL: {args.shell}")
    if args.directories:
        print(f"ARCHIVO_DIRECTORIOS: {args.directories}\n")
    else:
        print(f"ARCHIVO_DIRECTORIOS: (No proporcionado)\n")
    print(f"{bar}\n")

    found_shells = []  # Lista para almacenar las URLs de shells encontradas

    args.threads = int(args.threads)
    
    # Leer nombres de shells desde el archivo
    with open(args.shell, "r") as shell_file:
        shells = shell_file.read().splitlines()

    # Usar threading para escanear shells
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_shell = {executor.submit(check_shell, args.url, shell): shell for shell in shells}
        for future in tqdm(as_completed(future_to_shell), total=len(future_to_shell), desc="Escaneando", unit="shells"):
            result = future.result()
            if result:
                found_shells.append(result)
                print(f"{process} {white}{result}{reset}")

    # Si se proporciona el archivo de directorios, escanear directorios
    if args.directories:
        with open(args.directories, "r") as dir_file:
            directories = dir_file.read().splitlines()

        # Usar threading para escanear directorios
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            future_to_dirs = {executor.submit(scan_directories, args.url, directories, shells): directories}
            for future in as_completed(future_to_dirs):
                found_shells.extend(future.result())

    # Imprimir resultados finales
    print(f"\n{bar}")
    print(f"\n{bold}Shells Encontradas:{reset}\n")
    for path in found_shells:
        path = re.sub(r'(http://[^/]+)/+', r'\1/', path)  # Normalizar URLs
        print(f"{green}{indicator} {path}{reset}")

    # Imprimir estadísticas
    total_shells = len(shells)
    found_count = len(found_shells)
    not_found_count = total_shells - found_count

    print(f"\n{bold}Total de shells en la lista:{reset} {total_shells}")
    print(f"{bold}Shells encontradas:{reset} {found_count}")
    print(f"{bold}Shells no encontradas:{reset} {not_found_count}")

    print(f"\n{info} {white}GITHUB OFICIAL: {green}https://github.com/JennValentine/Webshell_Scanner{reset}")
    print(f"\n{bar}")

    # Guardar salida en un archivo si se especifica
    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write("\n".join(found_shells) + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{error} Interrupción por teclado: Operación cancelada. Saliendo...")
        sys.exit(0)
