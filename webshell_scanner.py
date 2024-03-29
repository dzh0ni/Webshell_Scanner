#!/usr/bin/env python3
#====================================================
#   SCRIPT:                   WEBSHELL SCANNER
#   DESARROLLADO POR:         JENN VALENTINE 
#   FECHA DE ACTUALIZACIÓN:   29-03-2024 
#   CONTACTO POR TELEGRAMA:   https://t.me/JennValentine
#   GITHUB OFICIAL:           https://github.com/JennValentine/Webshell_Scanner
#====================================================
import argparse
import requests
from urllib.parse import urljoin
from tqdm import tqdm
from datetime import datetime

# Colores
RESET = '\033[0m'
BOLD = '\033[1m'
GREEN = '\033[92m'
RED = '\033[91m'
YELLOW = '\033[93m'
BLUE = '\033[94m'
MAGENTA = '\033[95m'
CYAN = '\033[96m'
WHITE = '\033[97m'


# Iconos
CHECKMARK = '[+]'
ERROR = '[-]'
INFO = '[*]'
PROCESS = '>>'

# Barra de separación
bar = f"{YELLOW}{'-' * 45}{RESET}"

def check_shell(url, shell):
    target_url = urljoin(url, shell)
    try:
        response = requests.head(target_url, allow_redirects=True)
        if response.status_code == 200:
            return target_url
    except requests.exceptions.RequestException:
        pass

def main():
    # Configuración del analizador de argumentos
    parser = argparse.ArgumentParser(description="Webshell Scanner")
    parser.add_argument("-u", "--url", help="URL del sitio web objetivo", required=True)
    parser.add_argument("-s", "--shell", help="Ruta del archivo que contiene la lista de nombres de shell", required=True)
    parser.add_argument("-o", "--output", help="Guardar la salida en un archivo", metavar="output_file")
    args = parser.parse_args()

    # Mostramos el encabezado similar a Dirb
    print(f"\n{bar}")
    print(f"{BOLD}WEBSHELL SCANNER v2.22{RESET}")
    print(f"{BOLD}By JENN VALENTINE {RESET}")
    print(f"{bar}\n")
    print(f"START_TIME: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")
    print(f"URL_BASE: {args.url}")
    print(f"WORDLIST_FILES: {args.shell}\n")
    print(f"{bar}\n")

    # Leemos la lista de nombres de shell desde el archivo
    with open(args.shell, "r") as shell_file:
        shells = shell_file.read().splitlines()

    found_shells = []  # Lista para almacenar las URL de las shells encontradas

    # Escaneo de las shells con una barra de progreso
    for shell in tqdm(shells, desc="Escaneando", unit="shells"):
        shell_path = check_shell(args.url, shell)
        if shell_path:
            found_shells.append(shell_path)
            print(f"{MAGENTA}{PROCESS} {shell_path}{RESET}")

    # Mostramos la barra de separación nuevamente
    print(f"\n{bar}")

    # Mostramos las shells encontradas
    print(f"\n{BOLD}Shells encontradas:{RESET}\n")
    for path in found_shells:
        print(f"{GREEN}{INFO} {path}{RESET}")

    # Mostramos estadísticas finales
    print(f"\n{BOLD}Total de shells escaneadas:{RESET} {len(shells)}")
    print(f"{BOLD}Shells encontradas:{RESET} {len(found_shells)}")
    print(f"{BOLD}Shells no encontradas:{RESET} {len(shells) - len(found_shells)}")

    print(f"\n{YELLOW}{INFO} GITHUB OFICIAL: {GREEN}https://github.com/JennValentine/Webshell_Scanner{RESET}")

    print(f"\n{bar}")

    # Guardamos la salida en un archivo si se especifica la opción -o
    if args.output:
        with open(args.output, "w") as output_file:
            for path in found_shells:
                output_file.write(f"{path}\n")

if __name__ == "__main__":
    main()
