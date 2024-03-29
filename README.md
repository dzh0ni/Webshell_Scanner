![logo](https://github.com/JennValentine/Webshell_Scanner/blob/main/Imagenes/webshell_scanner.jpg)

# Webshell Scanner

## :information_source: Descripción
Este script en Python es un escáner de webshells que se encarga de identificar 
la presencia de webshells en un sitio web dado. Utiliza una lista de nombres 
de archivos comunes asociados con webshells y realiza solicitudes HTTP para 
verificar su existencia en el sitio web objetivo. Una vez encontradas, 
muestra las URL de las webshells encontradas.

## :arrow_down: Instalacion

1. Clona este repositorio en tu máquina:

    ```python
    sudo git clone https://github.com/JennValentine/Webshell_Scanner.git
    ```
2. Navega al directorio del repositorio:
    ```python3
    cd Webshell_Scanner
    python3 -m pip install -r requirements.txt
    ```
3. Instalación de requerimientos:
    ```python3
    python3 -m pip install -r requirements.txt
    ```

## :hammer: Modo de Uso

Ejecutar el script con la siguiente sintaxis:

```python
python3 webshell_scanner.py -u URL -s WORDLIST_FILE [-o OUTPUT_FILE]
```

* -u o --url: Especifica la URL del sitio web objetivo.
* -s o --shell: Especifica la ruta al archivo que contiene una lista de nombres de archivos de webshells.
* -o o --output (opcional): Permite guardar la salida en un archivo.

Ejemplo de uso básico:

```python
python3 webshell_scanner.py -u http://example.com -s shelllist.txt
```

Ejemplo con guardado de salida:

```python
python3 webshell_scanner.py -u http://example.com -s shelllist.txt -o found_shells.txt
```

## :busstop: Ayuda 

Ejecutar el script con argumentos -h, --help para desplegar la ayauda de argumentos:

```python
python3 webshell_scanner.py -h
```

---------------------------------------------------------------------------------------
```python
usage: webshell_scanner.py [-h] -u URL -s SHELL [-o output_file]

Webshell Scanner

options:
  -h, --help            show this help message and exit
  -u URL, --url URL     URL del sitio web objetivo
  -s SHELL, --shell SHELL
                        Ruta del archivo que contiene la lista de nombres de shell
  -o output_file, --output output_file
                        Guardar la salida en un archivo
```
---------------------------------------------------------------------------------------

:bookmark_tabs: Este script realiza solicitudes HTTP para verificar la existencia de webshells en un sitio web. 
Úsalo con precaución y asegúrate de tener permiso para escanear el sitio web objetivo.

## :octocat: Créditos
1. [Jenn Valentine](https://t.me/JennValentine) - Update Contributor
