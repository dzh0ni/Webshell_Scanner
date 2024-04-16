![logo](https://edteam-media.s3.amazonaws.com/blogs/big/2ab53939-9b50-47dd-b56e-38d4ba3cc0f0.png)

# Webshell Scanner

## :information_source: Descripción
Este script en Python es un escáner de webshells que se encarga de identificar 
la presencia de webshells en un sitio web dado. Utiliza una lista de nombres 
de archivos comunes asociados con webshells y realiza solicitudes HTTP para 
verificar su existencia en el sitio web objetivo. Una vez encontradas, 
muestra las URL de las webshells encontradas, ademas cuenta con una herramienta 
complementaria un script para realizar un escaneo de directorios utilizando Dirb.

## :arrow_down: Instalacion

1. Clona este repositorio en tu máquina:
    ```python
    sudo git clone https://github.com/JennValentine/Webshell_Scanner.git
    ```
2. Navega al directorio del repositorio:
    ```python
    cd Webshell_Scanner
    ```
3. Instalación de requerimientos:
    ```python
    python3 -m pip install -r requirements.txt
    ```
## :hammer: Modo de Uso

Ejecutar el script con la siguiente sintaxis:

```python
webshell_scanner.py [-h] -u URL -s SHELL [-d DIRECTORIES] [-o output_file]
```
Argumentos:

* -u URL, --url URL: Especifica la URL del sitio web objetivo.
* -s SHELL_FILE, --shell SHELL_FILE: Especifica la ruta del archivo que contiene la lista de nombres de shell.
* -d DIRECTORIES_FILE, --directories DIRECTORIES_FILE: (Opcional) Especifica la ruta del archivo que contiene los directorios a escanear en busca de shells.
* -o OUTPUT_FILE, --output OUTPUT_FILE: (Opcional) Guarda la salida en un archivo.

Ejemplo de uso:

```python
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt
```

Ejemplo de uso con guardado de salida:

```python
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -o found_shells.txt
```

Ejemplo de uso con directorios guardados por 'dirb script':
```python
python3 webshell_scanner.py -u http://192.168.19.171/ -s shelllist.txt -d directorios_encontrados.txt
```

Ejemplo de uso con directorios guardados por 'dirb script' con guardado de salida:

```python
python3 webshell_scanner.py -u http://192.168.19.171/ -s shelllist.txt -d directorios_encontrados.txt -o found_shells.txt
```
![logo](https://github.com/JennValentine/Webshell_Scanner/blob/main/Imagenes/webshell_scanner.jpg)

## :busstop: Ayuda 

Ejecutar el script con argumentos -h, --help para desplegar la ayauda de argumentos:

```python
python3 webshell_scanner.py -h
```
---------------------------------------------------------------------------------------
```python                                
sage: webshell_scanner.py [-h] -u URL -s SHELL [-d DIRECTORIES] [-o output_file]

Webshell Scanner

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL del sitio web objetivo
  -s SHELL, --shell SHELL
                        Ruta del archivo que contiene la lista de nombres de shell
  -d DIRECTORIES, --directories DIRECTORIES
                        Ruta del archivo que contiene los directorios a escanear
  -o output_file, --output output_file
                        Guardar la salida en un archivo

```
---------------------------------------------------------------------------------------

:bookmark_tabs: Este script realiza solicitudes HTTP para verificar la existencia de webshells en un sitio web. 
Úsalo con precaución y asegúrate de tener permiso para escanear el sitio web objetivo.

## :octocat: Créditos
1. [Jenn Valentine](https://t.me/JennValentine) - Update Contributor
