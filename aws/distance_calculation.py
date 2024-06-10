from math import radians, sin, cos, sqrt, atan2

# radius of earth in km
radius_of_earth = 6371.0088

# function to calculate distance using latitude and longitude
def calculate_distance(lat1, lon1, lat2, lon2):
    # convert degrees to radians
    lat1, lon1, lat2, lon2 = map(radians, [lat1, lon1, lat2, lon2])

    # calculate distance
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
    c = 2 * atan2(sqrt(a), sqrt(1 - a))

    distance = radius_of_earth * c
    return distance