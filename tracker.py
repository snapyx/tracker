import phonenumbers
from phonenumbers import carrier
from phonenumbers import geocoder
from geopy.geocoders import  Nominatim

#pnm = ""#input("Enter pnm: ")

#nmb = phonenumbers.parse(pnm)
#cntr =  geocoder.description_for_number(nmb , 'en')
#print(cntr)
#operat = carrier.name_for_number(nmb , 'en')
#print(operat)

#geoloc = Nominatim(user_agent="geoapiExercises")
#locatio = geoloc.geocode(cntr)

#lng = locatio.longitude
#lat = locatio.latitude
#print(lng , lat)

def getNmLocation(number):
    nmb = phonenumbers.parse(number)
    country = geocoder.description_for_number(nmb, 'en')
    operator = carrier.name_for_number(nmb, 'en')
    geolocation = Nominatim(user_agent="geoapiExercises")
    location = geolocation.geocode(country)
    latitude = location.latitude
    longitude = location.longitude
    return [country, operator, latitude, longitude]
    