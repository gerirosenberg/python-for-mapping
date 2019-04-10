# This program describes a longitude and latitude point.

# Says what the program will help the user do, followed by an empty line
print("This program provides information about a location based on its longitude and latitude.")
print()

# Uses the latitude to determine location details
def latInfo() :
    lat = float(input("Please enter the latitude of the location: "))
    if lat == 0.0:
        print('That location is on the equator.')
    elif 0.0 < lat <= 90.0:
        print('That location is north of the equator.')
    elif -90.0 <= lat < 0.0:
        print('That location is south of the equator.')
        
    # Restarts the function if the latitude is invalid
    else:
        print('That location does not have a valid latitude.')
        latInfo()
        
# Uses the longitude to determine location details
def longInfo() :
    long = float(input("Please enter the longitude of the location: "))
    if long == 0.0:
        print('That location is on the prime meridian.')
    elif 0.0 < long <= 180.0:
        print('That location is east of the prime meridian.')
    elif -180.0 <= long < 0.0:
        print('That location is west of the prime meridian.')
        
    # Restarts the function if the longitude is invalid
    else:
        print('That location does not have a valid longitude.')
        longInfo()

# Runs the latitude and longitude functions
latInfo()
longInfo()
