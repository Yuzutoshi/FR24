import time
from datetime import datetime

flights = []; timestamps=[]
for i in range(60*6*4): # Retrieve once every 10 seconds for 60 minutes
    flights.append(fr_api.get_flights(bounds=bounds))
    timeStamps.append(datetime.now())
    time.sleep(10)
    