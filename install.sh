#!/bin/bash

git clone https://github.com/AAAAAEXQOSyIpN2JZ0ehUQ/Webshell_Scanner.git
chmod +x Webshell_Scanner/*
cd Webshell_Scanner
ls -ltha
sudo python3 -m pip install -r requirements.txt 
sudo apt installl -y dirb nmap arp-scan 


