# This program calculates the distance between two locations based on their latitude and longitude.

#Imports the math module
import math

# Says what the program will help the user do, followed by an empty line
print("This program calculates the distance between two locations based on their longitude and latitude.")
print()
    
# Creates a function to prep the user input for calculations
def get_coord(question_text, coord_min, coord_max):
    
    # Sets the user input to the variable coord
    coord = input(question_text)
    
    # Check if coord is a number
    try:
        coord = float(coord)

    # Restarts if coord cannot be converted to a float
    except:
        print('Your coordinates are invalid. Please re-enter your coordinates.')
        get_coord(question_text, coord_min, coord_max)

    # Restarts if coord is not within the correct minimum and maximum value
    if not coord_min <= coord <= coord_max:
        print('Your coordinates are invalid. Please re-enter your coordinates.')
        get_coord(question_text, coord_min, coord_max)

    # Converts coord to radians to prep for calculations
    return math.radians(coord)

# Uses the function get_coord for each part of each coordinate while setting the minimum and maximum values
# Sets each result to the appropriate variable for later calculations
lat1 = get_coord("What is the latitude of the first location? ", -90.0, 90.0)
long1 = get_coord("What is the longitude of the first location? ", -180.0, 180.0)
lat2 = get_coord("What is the latitude of the second location? ", -90.0, 90.0)
long2 = get_coord("What is the longitude of the second location? ", -180.0, 180.0)
            
# Calculates the distance using the spherical distance formula
dist = 6300 * math.acos((math.sin(lat1) * math.sin(lat2)) + (math.cos(lat1) * math.cos(lat2) * math.cos(long1 - long2)))

# Displays the results of the calcuations
print("The distance between those two locations is", dist, "km.")
