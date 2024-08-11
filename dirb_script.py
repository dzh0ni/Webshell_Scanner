#!/usr/bin/env python3
#====================================================
#   SCRIPT:                   DIRB SCRIPT - WEBSHELL SCANNER
#   DEVELOPED BY:             JENN VALENTINE 
#   LAST UPDATED:             29-03-2024 
#   CONTACT ON TELEGRAM:      https://t.me/JennValentine
#   OFFICIAL GITHUB:           https://github.com/JennValentine/Webshell_Scanner
#====================================================

# Importing necessary modules
import subprocess
import sys
import re
import time

# Color palette
reset = "\033[0m"       # Reset all styles and colors
bold = "\033[1m"        # Bold text
italic = "\033[3m"      # Italic text
underline = "\033[4m"   # Underlined text
blink = "\033[5m"       # Blinking text
reverse = "\033[7m"     # Invert background and text colors
hidden = "\033[8m"      # Hidden text (usually invisible)

# Text colors
black = "\033[0;30m"     # Black
red = "\033[0;31m"       # Red
green = "\033[0;32m"     # Green
yellow = "\033[0;33m"    # Yellow
blue = "\033[0;34m"      # Blue
magenta = "\033[0;35m"   # Magenta
cyan = "\033[0;36m"      # Cyan
white = "\033[0;37m"     # White

# Background colors
bg_black = "\033[0;40m"     # Black background
bg_red = "\033[0;41m"       # Red background
bg_green = "\033[0;42m"     # Green background
bg_yellow = "\033[0;43m"    # Yellow background
bg_blue = "\033[0;44m"      # Blue background
bg_magenta = "\033[0;45m"   # Magenta background
bg_cyan = "\033[0;46m"      # Cyan background
bg_white = "\033[0;47m"     # White background

# Icons
checkmark = f"{white}[{green}++{white}]{green}"
error = f"{white}[{red}--{white}]{reset}"
info = f"{white}[{yellow}**{white}]{white}"
unknown = f"{white}[{blue}!!{white}]{reset}"
process = f"{white}[{magenta}>>{white}]{magenta}"
indicator = f"{red}==>{reset}"


# Separator bar
barra = f"{blue}|--------------------------------------------|{reset}"
bar = f"{yellow}{'-' * 45}{reset}"

def run_dirb(url):
    # Run Dirb and capture the output
    print(f"\n{process} {white}Running Dirb on {url}...")
    process = subprocess.Popen(['dirb', url], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
    stdout, stderr = process.communicate()

    if process.returncode == 0:
        print(f"{checkmark} Dirb ran successfully.\n")
        # Filter lines containing "DIRECTORY" or "CODE:200"
        directories = [re.search(r'http://\S+', line).group() for line in stdout.split('\n') if '==> DIRECTORY:' in line]
        files = [re.search(r'http://\S+', line).group() for line in stdout.split('\n') if 'CODE:200' in line]
        return directories, files
    else:
        print(f"{error} Error running Dirb:")
        print(stderr)
        return [], []

def save_to_txt(data, file):
    with open(file, 'w') as f:
        for item in data:
            f.write(item + '\n')
            print(f"{checkmark} Saved to {file}: {item}")
            time.sleep(0.1)  # Simulate a longer writing process
    print(f"\n{info} Data has been saved to {file}\n")
    print(bar)

def KeyboardInterruptHandler(signal, frame):
    print(f"\n\n{error} KeyboardInterrupt Operation cancelled. Exiting the program...")
    sys.exit(0)

if __name__ == "__main__":
    # Handle KeyboardInterrupt
    import signal
    signal.signal(signal.SIGINT, KeyboardInterruptHandler)
    
    # Check the number of arguments
    if len(sys.argv) != 2:
        print(f"\n{info} {green}Usage: python3 dirb_script.py <URL>")
        sys.exit(1)

    url = sys.argv[1]
    directories_file = "directories_found.txt"
    files_file = "files_found.txt"

    directories_found, files_found = run_dirb(url)

    if directories_found:
        print(bar)
        print(f"\n{info} Directories found:\n")
        save_to_txt(directories_found, directories_file)
    else:
        print(f"{error} No directories found.")

    if files_found:
        print(f"\n{info} Files found:\n")
        save_to_txt(files_found, files_file)
    else:
        print(f"{error} No files found.")
