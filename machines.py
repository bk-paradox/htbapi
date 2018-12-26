from htb_class import *
import os
import subprocess
from time import sleep

paradox = HTB("config")
paradox.init()
test = paradox.get_machines()

path = os.getcwd()
print("Current working directory and base path is %s" % path)
#create directory structure and run nmap scan
for t in range(len(test[0][1])):
    machine = test[0][1][t].strip()
    print "[*] Name: " + machine 
    try:
        machine_path = path + '/' + machine
        os.mkdir(machine_path)
    except:
        print(colour['fail'] + "[-] Failed to create directory %s" % machine_path)
    else:
        print(colour['green'] + "[+] Successfully created directory %s" % machine_path)
        ip = test[3][1][t].strip()
        print(colour['green'] + "[*] NMAP Scanning %s for tcp/udp services: " + ip ) 
        os.chdir(machine_path)
        #Run nmap and background process
        tcp_command = 'nmap -sC -sV -oA tcp ' + ip
        subprocess.Popen(tcp_command, shell=True, close_fds=True)
        #Run nmap and background process
        udp_command = 'nmap -sC -sU -oA udp --top-ports 100 ' + ip
        subprocess.Popen(udp_command, shell=True, close_fds=True)
        print(colour['blue'] + "[*] Sleeping for 100 seconds before running next nmap")
        sleep(100)

print("[+] Initial enumeration complete, happy hunting!")
