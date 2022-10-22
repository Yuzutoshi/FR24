from flightradar24.api \
import Flightradar24API
import folium

bounds="60,22,113,176"
fr_api=Flightradar24API()
flights=fr_api.get_flights(
    bounds=bounds)
fmap = folium.Map(
 location=[35,135],zoom_start=3)
for f in flights:
    folium.Marker(
 locatin=[f.latitude,f.longitude],
 icon=folium.ICON(icon="plane")
    ).add_to(fmap)
fmap
    