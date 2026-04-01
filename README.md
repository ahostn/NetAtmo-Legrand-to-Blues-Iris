# NetAtmo2BlueIris
Show your Netatmo Presence camera feed in Blue Iris

INSTALL:

install python3

clone lnetatmo repo

save and fix readCam.py

open BlueIris and add Generic/ONViF cammera and set camera name (short name used later!)

create file .netatmo.credentials in your home durectory (C:\Users\ahostn\.netatmo.credentials)

Open file and paste this:

{

 "CLIENT_ID": "",
 
 "CLIENT_SECRET": "",
 
 "REFRESH_TOKEN": ""
 
}


Go to https://dev.netatmo.com/apps/ and register new app to access your cam.

Create task to run as ADMIN every 10 minutes and run readCam.py!
