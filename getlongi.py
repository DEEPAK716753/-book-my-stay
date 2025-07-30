from geopy.geocoders import OpenCage
import time 

def get_coordinates(location_name):
    print("find longitude latitude of locations....")
    geolocator = OpenCage(api_key='b9ea0a9b02c04200a64cb4e602e6591e')
    time.sleep(2)
    location = geolocator.geocode(location_name)
    if location:
        return location.latitude, location.longitude
    else:
        return None

# location_name = "Jalandhar bus stand"
# coordinates = get_coordinates(location_name)

# if coordinates:
#     print(f"The latitude and longitude of {location_name} are {coordinates[0]} and {coordinates[1]} respectively.")
# else:
#     print(f"Coordinates for {location_name} not found.")

