#!/usr/bin/env python3

#====================================================
#
#   SCRIPT:                   Webshell Scanner
#   DEVELOPED BY:             dZh0ni - Jony Rivera 
#   LAST UPDATED:             03-29-2024 
#   CONTACT VIA TELEGRAM:     https://t.me/dZh0ni_Dev
#   OFFICIAL GITHUB:          https://github.com/dzh0ni/Webshell_Scanner
#
#	Modified by: Lance Kenji
#	Github: https://github.com/lancekenji
#	Contact: https://t.me/lance_aswwscxzc
#	v1 - English Translation | Threading Implementation using `concurrent`
#
#====================================================

# Import necessary modules
import argparse  # For parsing command-line arguments
import requests  # For making HTTP requests
import re  # For working with regular expressions
from urllib.parse import urljoin  # For joining URLs
from tqdm import tqdm  # For displaying a progress bar
from datetime import datetime  # For getting the current date and time
import sys  # For handling Ctrl + C interruption
from concurrent.futures import ThreadPoolExecutor, as_completed  # For threading

# Color palette
reset = "\033[0m"       # Reset all styles and colors
bold = "\033[1m"        # Bold text
italic = "\033[3m"      # Italic text
underline = "\033[4m"   # Underlined text
blink = "\033[5m"       # Blinking text
reverse = "\033[7m"     # Inverted colors
hidden = "\033[8m"      # Hidden text (typically invisible)

# Text colors
black = "\033[0;30m"    # Black
red = "\033[0;31m"      # Red
green = "\033[0;32m"    # Green
yellow = "\033[0;33m"   # Yellow
blue = "\033[0;34m"     # Blue
magenta = "\033[0;35m"  # Magenta
cyan = "\033[0;36m"     # Cyan
white = "\033[0;37m"    # White

# Background colors
bg_black = "\033[0;40m"    # Black background
bg_red = "\033[0;41m"      # Red background
bg_green = "\033[0;42m"    # Green background
bg_yellow = "\033[0;43m"   # Yellow background
bg_blue = "\033[0;44m"     # Blue background
bg_magenta = "\033[0;45m"  # Magenta background
bg_cyan = "\033[0;46m"     # Cyan background
bg_white = "\033[0;47m"    # White background

# Icons
checkmark = f"{white}[{green}++{white}]{green}"
error = f"{white}[{red}--{white}]{reset}"
info = f"{white}[{yellow}**{white}]{white}"
unknown = f"{white}[{blue}!!{white}]{reset}"
process = f"{white}[{magenta}>>{white}]{magenta}"
indicator = f"{red}==>{reset}"

# Separators
separator = f"{blue}|{'-' * 44}|{reset}"
bar = f"{yellow}{'-' * 45}{reset}"

# Function to check if a shell exists at a URL
def check_shell(base_url, shell_name):
    target_url = urljoin(base_url, shell_name)
    try:
        response = requests.head(target_url, allow_redirects=True)
        if response.status_code == 200:
            return target_url
    except requests.RequestException:
        pass
    return None

# Function to scan directories for shells
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

# Main function
def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Webshell Scanner")
    parser.add_argument("-u", "--url", help="Target website URL", required=True)
    parser.add_argument("-s", "--shell", help="File containing shell names", required=True)
    parser.add_argument("-d", "--directories", help="File containing directories to scan", default=None)
    parser.add_argument("-t", "--threads", help="Threads (default: 10)", default=10)
    parser.add_argument("-o", "--output", help="Save output to a file", metavar="output_file")
    args = parser.parse_args()

    # Print script information
    print(f"\n{bar}")
    print(f"{bold}WEBSHELL SCANNER v1.00{reset}")
    print(f"{bold}By JENN VALENTINE{reset}")
    print(f"{bar}\n")
    print(f"START_TIME: {datetime.now().strftime('%a %b %d %H:%M:%S %Y')}")
    print(f"BASE_URL: {args.url}")
    print(f"SHELL_LIST_FILE: {args.shell}")
    if args.directories:
        print(f"DIRECTORIES_FILE: {args.directories}\n")
    else:
        print(f"DIRECTORIES_FILE: (Not provided)\n")
    print(f"{bar}\n")

    found_shells = []  # List to store found shell URLs

    args.threads = int(args.threads)
    
    # Read shell names from file
    with open(args.shell, "r") as shell_file:
        shells = shell_file.read().splitlines()

    # Use threading to scan shells
    with ThreadPoolExecutor(max_workers=args.threads) as executor:
        future_to_shell = {executor.submit(check_shell, args.url, shell): shell for shell in shells}
        for future in tqdm(as_completed(future_to_shell), total=len(future_to_shell), desc="Scanning", unit="shells"):
            result = future.result()
            if result:
                found_shells.append(result)
                print(f"{process} {white}{result}{reset}")

    # If directories file is provided, scan directories
    if args.directories:
        with open(args.directories, "r") as dir_file:
            directories = dir_file.read().splitlines()

        # Use threading to scan directories
        with ThreadPoolExecutor(max_workers=args.threads) as executor:
            future_to_dirs = {executor.submit(scan_directories, args.url, directories, shells): directories}
            for future in as_completed(future_to_dirs):
                found_shells.extend(future.result())

    # Print final results
    print(f"\n{bar}")
    print(f"\n{bold}Found Shells:{reset}\n")
    for path in found_shells:
        path = re.sub(r'(http://[^/]+)/+', r'\1/', path)  # Normalize URLs
        print(f"{green}{indicator} {path}{reset}")

    # Print statistics
    total_shells = len(shells)
    found_count = len(found_shells)
    not_found_count = total_shells - found_count

    print(f"\n{bold}Total shells in list:{reset} {total_shells}")
    print(f"{bold}Possible shells found:{reset} {found_count}")
    print(f"{bold}Shells not found:{reset} {not_found_count}")

    print(f"\n{info} {white}OFFICIAL GITHUB: {green}https://github.com/JennValentine/Webshell_Scanner{reset}")
    print(f"\n{bar}")

    # Save output to file if specified
    if args.output:
        with open(args.output, "w") as output_file:
            output_file.write("\n".join(found_shells) + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print(f"\n\n{error} KeyboardInterrupt: Operation cancelled. Exiting...")
        sys.exit(0)
