from flightradar24.api \
import FlightRadar24API
import folium

# Area to get aeronautical information
bounds="60,22,113,176"
fr_api=FlightRadar24API()
flights=fr_api.get_flights(
            bounds=bounds)
fmap = folium.Map(
    location=[35,135],zoom_start=3)
for f in flights:
    folium.Map(
        location=[35,135],zoom_start=3)
for f in flights:
    folium.Marker(  # Marker prot
        location=[f.latitude,f.longitude],
        icon=folium.Icon(icon="plane")
        ).add_to(fmap)
fmap    # Map Display

import time
from datetime import datetime


flights = []; timestamps=[]
for i in range(60*6*4): # Retrieve once every 10 seconds for 60 minutes
    flights.append(fr_api.get_flights(bounds=bounds))
    timestamps.append(datetime.now())
    time.sleep(10)
    

