![logo](https://edteam-media.s3.amazonaws.com/blogs/big/2ab53939-9b50-47dd-b56e-38d4ba3cc0f0.png)

# Webshell Scanner

## :information_source: Description
This Python script is a webshell scanner that identifies the presence of webshells on a given website. It uses a list of common webshell file names and makes HTTP requests to check their existence on the target website. Once found, it displays the URLs of the detected webshells. Additionally, it includes a complementary tool, a script for directory scanning using Dirb.

## :computer: Installation

1. Clone this repository to your machine:
    ```bash
    git clone https://github.com/JennValentine/Webshell_Scanner.git
    ```
2. Navigate to the repository directory:
    ```bash
    cd Webshell_Scanner
    ```
3. Install the requirements:
    ```bash
    python3 -m pip install -r requirements.txt
    ```

## :computer: One-Line Installation
```bash
wget https://raw.githubusercontent.com/JennValentine/Webshell_Scanner/main/install.sh; sudo chmod +x install.sh; sudo ./install.sh; sudo rm -rf install.sh
```

## :sos: Help

Run the script with the `-h` or `--help` arguments to display help about arguments:

```bash
python3 webshell_scanner.py -h
```

```
webshell_scanner.py [-h] -u URL -s SHELL [-d DIRECTORIES] [-o output_file]

Arguments:

* -u URL, --url URL: Specifies the target website URL.
* -s SHELL_FILE, --shell SHELL_FILE: Specifies the path to the file containing the list of shell names.
* -d DIRECTORIES_FILE, --directories DIRECTORIES_FILE: (Optional) Specifies the path to the file containing directories to scan for shells.
* -t THREADS, --threads THREADS: Number of threads (default: 10).
* -o OUTPUT_FILE, --output OUTPUT_FILE: (Optional) Saves the output to a file.
```

## :rocket: How to Use the Webshell Scanner

To use the webshell scanner, run the `webshell_scanner.py` script from the command line with appropriate parameters, such as the target website URL and the path to the webshell file list.

Example usage:

```bash
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt
```

Example usage with output file:

```bash
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -o found_shells.txt
```

Example usage with directories saved by the 'dirb script':

```bash
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -d directories_found.txt
```

Example usage with directories saved by the 'dirb script' and output file:

```bash
python3 webshell_scanner.py -u http://example.com/ -s shelllist.txt -d directories_found.txt -o found_shells.txt
```

![logo](https://github.com/JennValentine/Webshell_Scanner/blob/main/Images/webshell_scanner.jpg)

:memo: Notes: The webshell scanner identifies the presence of webshells on a given website. It uses a list of common webshell file names and makes HTTP requests to check their existence on the target website. Once found, it displays the URLs of the detected webshells.

## :rocket: How to Use the Dirb Script

To use the Dirb script, run the `dirb_script.py` from the command line with the URL of the website you wish to scan as the only argument.

Example usage:

```bash
python3 dirb_script.py http://example.com/
```

![logo](https://github.com/JennValentine/Webshell_Scanner/blob/main/Images/dirb_script.jpg)

:memo: Notes: The Dirb script is used to perform directory scanning on a specified URL. It uses the Dirb tool to perform the scan and captures the directories and files found during the process. The results are saved in text files for further analysis.

## :email: Contact
* :busts_in_silhouette: [Jenn Valentine](https://t.me/JennValentine) - Update Contributor :octocat:

## 🌐 Translated by
* 👥 [Lance Kenji](https://t.me/lance_aswwscxzc)
