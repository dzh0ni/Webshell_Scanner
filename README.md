![logo](https://multianime.com.mx/wp-content/uploads/2020/08/anime-404-gomen-.jpg)

# Webshell Scanner :octocat:

## :information_source: Descripción
Este script en Python es un escáner de webshells que se encarga de identificar 
la presencia de webshells en un sitio web dado. Utiliza una lista de nombres 
de archivos comunes asociados con webshells y realiza solicitudes HTTP para 
verificar su existencia en el sitio web objetivo. Una vez encontradas, 
muestra las URL de las webshells encontradas, ademas cuenta con una herramienta 
complementaria un script para realizar un escaneo de directorios utilizando Dirb.

## :computer: Instalación
```python
git clone https://github.com/dzh0ni/Webshell_Scanner.git
chmod +x Webshell_Scanner/*
cd Webshell_Scanner
ls -ltha
```

## :package: Paquete
```python
sudo python3 -m pip install -r requirements.txt 
```
```python
sudo apt install -y dirb
```

## :computer: Instalación en una Línea
```bash
sudo wget https://raw.githubusercontent.com/dzh0ni/Webshell_Scanner/main/install.sh -O - | sudo bash && sudo rm -rf wget-log*
```

## :sos: Ayuda 

Ejecutar el script con argumentos -h, --help para desplegar la ayauda de argumentos:

```python
python3 webshell_scanner.py --help
```
```
usage: webshell_scanner.py [-h] -u URL -s SHELL [-d DIRECTORIES] [-o output_file]

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

## :rocket: Modo de Uso
**webshell scanner**

Para utilizar el webshell scanner, ejecuta el script webshell_scanner.py desde la línea de comandos con los parámetros adecuados, como la URL del sitio web objetivo y la ruta del archivo de lista de nombres de archivos de webshells.

Ejemplo de uso:

```python
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt
```

Ejemplo de uso con guardado de salida:

```python
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -o Posibles_shells.txt
```

Ejemplo de uso con directorios guardados por 'dirb script':
```python
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -d directorios_encontrados.txt
```

Ejemplo de uso con directorios guardados por 'dirb script' con guardado de salida:

```python
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -d directorios_encontrados.txt -o Posibles_shells.txt
```
![logo](https://github.com/dzh0ni/Webshell_Scanner/blob/main/Imagenes/webshell_scanner.jpg)

:memo: Notas: El webshell scanner se encarga de identificar la presencia de webshells en un sitio web dado. Utiliza una lista de nombres de archivos comunes asociados con webshells y realiza solicitudes HTTP para verificar su existencia en el sitio web objetivo. Una vez encontradas, muestra las URL de las webshells encontradas.

## :rocket: Modo de Uso 
**dirb script**

Para utilizar el dirb script, ejecuta el script dirb script desde la línea de comandos con la URL del sitio web que deseas escanear como único argumento.

Ejemplo de uso:

```python
python3 dirb_script.py http://example.com/
```
![logo](https://github.com/dzh0ni/Webshell_Scanner/blob/main/Imagenes/dirb_script.jpg)
:memo: El dirb script se utiliza para realizar un escaneo de directorios en una URL especificada. Utiliza la herramienta Dirb para realizar el escaneo y captura los directorios y archivos encontrados durante el proceso. Los resultados se guardan en archivos de texto para su posterior análisis.

## :hammer_and_wrench: Requisitos 

- Sistema Operativo: Linux/Unix
- Dependencias: Python3, Bash, requests y tqdm

## :open_file_folder: Estructura del Repositorio

| Icono            | Nombre              | Descripción                                      |
|------------------|---------------------|--------------------------------------------------|
| :file_folder:    | Imagenes            | Carpeta que contiene imágenes del script en ejecución |
| :page_facing_up: | LICENSE             | Archivo de licencia MIT para el proyecto         |
| :book:           | README.md           | Archivo README con la documentación del proyecto |
| :page_facing_up: | dirb_script.py      | Script Python que realiza un escaneo utilizando Dirb |
| :package:        | install.sh          | Script de instalación automatizada               |
| :package:        | requirements.txt    | Archivo con las dependencias necesarias para ejecutar el proyecto |
| :book:           | shelllist.txt       | Lista de nombres comunes de webshells para el escaneo |
| :page_facing_up: | webshell_scanner.py | Script Python principal que realiza la detección de webshells |

## :star2: Contribuciones

Las contribuciones son bienvenidas. Si tienes ideas para mejorar este script o encuentras algún problema, siéntete libre de abrir un *pull request* o *issue*.

## :warning: Advertencias

- Uso Responsable: Este script está diseñado para ser utilizado en dispositivos y redes que te pertenecen o para las que tienes permiso de uso. No lo utilices para actividades no autorizadas.

## :email: Contacto 
* :busts_in_silhouette: **dZh0ni**: [Telegram](https://t.me/dZh0ni_Dev) - Desarrollador Webshell Scanner
* :busts_in_silhouette: **JennValentine**: ![Telegra](https://t.me/JennValentine) - Desarrollador Webshell Scanner 
* :busts_in_silhouette: **LanceKenji**: ![GitHub](https://github.com/lancekenji) - English Translations and Threading Implmentations 
