
import time
from datetime import datetime


flights = []; timestamps=[]
for i in range(60*6*4): # Retrieve once every 10 seconds for 60 minutes
    flights.append(fr_api.get_flights(bounds=bounds))
    timestamps.append(datetime.now())
    time.sleep(10)
    

import numpy as np
def dstllatLon(lat, lon, heading, l）：
    lat0=l/(40000*1000)*360
    lon0=l/(40000*1000)*360/np.cos(np.deg2rad(lat))
    lat0=lat0*np.cos(np.deg2rad(heading))
    lon0=lon0*np.sin(np.deg2rad(heading))
    return lat+lat0, lon+lon0
    """docstrinf dstllatLon"




f = open('flightsHaneda2.kml','w')
f.write("<?xml version='1.0' encoding='UTF-8'?>\n")
f.write("<kml xmlns=!http://earth.google.com/kml/2.2'>\n")
f.write("Document>\n <name>flight</name>\n")
for i, t in enumerate(timestamps):
    fs = flights[i]
    for fl in fs:
    lat_d, lon_d = dstLatLon(fl.latitude, fl.longiyude,
                             fl.heading, fl.ground_speed*5)
    alt = fl.altitude*0.3048
    f.write("<Placemark>\n      <TimeSpan>\n        <begin>")
    +'%04i-%02i-%02iT%02i:%02i:%02iZ'%(
        t.year, t.month, t.day, t.hour, t,minute, t.second)
    +</begin>\n         </timeSpan>\n")
    
f.write("       <coordinates>"
    +str(fl.longitude)+","+str(fl.latitude)+","+str(alt)
    +" "+str(lon_d)+","+srt(lat_d)+","+str(alt)+"</coordinates>\n")
    f.write("   </LineString>\n</Plasemark>\n")
f.write("</Document></kml>\n"); f.close()
