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

## :busstop: Ayuda 

Ejecutar el script con argumentos -h, --help para desplegar la ayauda de argumentos:

```python
python3 webshell_scanner.py -h
```
```
webshell_scanner.py [-h] -u URL -s SHELL [-d DIRECTORIES] [-o output_file]

Argumentos:

* -u URL, --url URL: Especifica la URL del sitio web objetivo.
* -s SHELL_FILE, --shell SHELL_FILE: Especifica la ruta del archivo que contiene la lista de nombres de shell.
* -d DIRECTORIES_FILE, --directories DIRECTORIES_FILE: (Opcional) Especifica la ruta del archivo que contiene los directorios a escanear en busca de shells.
* -o OUTPUT_FILE, --output OUTPUT_FILE: (Opcional) Guarda la salida en un archivo.
```

## :hammer: Modo de Uso para webshell scanner

Para utilizar el escáner de webshells, ejecuta el script webshell_scanner.py desde la línea de comandos con los parámetros adecuados, como la URL del sitio web objetivo y la ruta del archivo de lista de nombres de archivos de webshells.

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
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -d directorios_encontrados.txt
```

Ejemplo de uso con directorios guardados por 'dirb script' con guardado de salida:

```python
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -d directorios_encontrados.txt -o found_shells.txt
```
![logo](https://github.com/JennValentine/Webshell_Scanner/blob/main/Imagenes/webshell_scanner.jpg)

:bookmark_tabs: El webshell scanner se encarga de identificar la presencia de webshells en un sitio web dado. Utiliza una lista de nombres de archivos comunes asociados con webshells y realiza solicitudes HTTP para verificar su existencia en el sitio web objetivo. Una vez encontradas, muestra las URL de las webshells encontradas.

## :hammer: Modo de Uso para dirb script

Para utilizar el script Dirb, ejecuta el script dirb_script.py desde la línea de comandos con la URL del sitio web que deseas escanear como único argumento.

Ejemplo de uso:

```python
python3 dirb_script.py http://example.com/
```
![logo](https://github.com/JennValentine/Webshell_Scanner/blob/main/Imagenes/dirb_script.jpg)

:bookmark_tabs: El Dirb script se utiliza para realizar un escaneo de directorios en una URL especificada. Utiliza la herramienta Dirb para realizar el escaneo y captura los directorios y archivos encontrados durante el proceso. Los resultados se guardan en archivos de texto para su posterior análisis.

## :octocat: Créditos
1. [Jenn Valentine](https://t.me/JennValentine) - Update Contributor
