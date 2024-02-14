from unittest import result
import phonenumbers
import folium
import opencage
from myphone import number
from phonenumbers import geocoder
from phonenumbers import carrier
from opencage.geocoder import OpenCageGeocode


pepnumber= phonenumbers.parse(number)
location= geocoder.description_for_number(pepnumber, "en")
print(location)

service_prov = phonenumbers.parse(number)
print(carrier.name_for_number(service_prov, "en"))

key = "9d6ea619f1554c69be231f1f6412a209"

geocoder= OpenCageGeocode(key)
query= str(location)
results= geocoder.geocode(query)

lat= results[0]["geometry"]["lat"]
lng= results[0]["geometry"]["lng"]
print(lat,lng)

myMap=folium.Map(location=[lat,lng],zoom_start=9)
folium.Marker([lat,lng],popup=location).add_to(myMap)
myMap.save("mylocation.htmt")