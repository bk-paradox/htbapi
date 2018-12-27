This project was started to just scrape the HTB machines list and run a simple nmap scan.

The machines.py script will create multiple directories in the current working directory for each machine.
It will then run an nmap scan for both tcp and udp using
nmap -sC -sV -oA tcp <ip addr>
and
nmap -sC -sU -oA udp --top-ports 100 <ip addr>

This is aimed at doing initial recon on all machines, to speed up triaging.

Functionality to add later:
if port 80 is detected run gobuster
accept command line argumenets to change directory to output to.
have command line argumenets to select machines to scan.

If you want to add to this very simple script, please feel free to pull
I am not a programmer, just do this for a hobby.

Regards
paradox.
