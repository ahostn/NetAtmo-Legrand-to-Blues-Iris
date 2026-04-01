#!/usr/bin/python3

# Locate the camera name "MyCam" IP on the local LAN
# to collect a snapshot of what the camera sees
# If available use a local connection to save internet bandwith


from sys import exit
import lnetatmo,json,winreg
import os
import re  

MY_CAMERA = "Kamera Name"
# Authenticate (see authentication in documentation)
# Note you will need the appropriate scope (read_welcome access_welcome or read_presence access_presence)
# depending of the camera you are trying to reach
# The default library scope ask for all aceess to all cameras
authorization = lnetatmo.ClientAuth()

# Gather Home information (available cameras and other infos)
homeData = lnetatmo.HomeData(authorization)
#print (vars(authorization))

# Gather Home information (available cameras and other infos)

url = homeData.rawData["homes"][0]['cameras'][0]
print(url)
url = (url.get('vpn_url')).replace("https://","admin@")
url = url.replace("netatmo.com","netatmo.com:443")
streamUrl = url+"/live/files/medium/index.m3u8/:554:1[]"

IPpath = streamUrl.replace("/live/files/medium/index.m3u8/:554:1[]","")
IP = re.findall("admin@(.*):443",streamUrl)
#IPpath = IPpath.replace(IP[0],"")
IPpath = IPpath.replace("admin@:443","")
IPpath = IPpath+"/live/files/medium/index.m3u8"
#IP = IP[0]
print ("IPpath = ",IPpath)
print ("Stream URL =",streamUrl)
print ("IP = ",IP)
vpn_url, local_url = homeData.cameraUrls()
print ("CAM URL = ",vpn_url)

# Open the key for the Blue Iris camera settings
key_path = r"SOFTWARE\Perspective Software\Blue Iris\Cameras\REPLACEnameHERE" #!!!! enter real cammera name here, add it to Blue Iris first!
key = winreg.OpenKey(winreg.HKEY_LOCAL_MACHINE, key_path, 0, winreg.KEY_ALL_ACCESS)

winreg.SetValueEx(key, "ip_path", 0, winreg.REG_SZ, IPpath)
winreg.SetValueEx(key, "dsname", 0, winreg.REG_SZ, streamUrl)
winreg.SetValueEx(key, "ip", 0, winreg.REG_SZ, IP)
# Close the registry key
winreg.CloseKey(key)

# Request a snapshot from the camera
snapshot = homeData.getLiveSnapshot( )

# If all was Ok, I should have an image, if None there was an error
if not snapshot :
    # Decide what to do with an error situation (alert, log, ...)
    exit(1)

# You can then archive the snapshot, send it by mail, message App, ...
# Example : Save the snapshot in a file
with open("MyCamSnap.jpg", "wb") as f: f.write(snapshot)

exit(0)
