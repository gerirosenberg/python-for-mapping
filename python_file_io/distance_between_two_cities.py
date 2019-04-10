# Reads CityPop, stores it in dictionaries, finds the great circle distance
# between two cities

import csv
import os.path
import math

filename = 'CityPop.csv'

# Make city_data into list
city_data = []

# If filename is bad, tell the user
if not os.path.isfile(filename):
    print("File does not exist.")

# Open CityPop using DictReader, which stores each row as a dictionary
with open(filename, 'r') as f:
    reader = csv.DictReader(f)

    # Make each row into a separate dictionary
    for row in reader:
        city_data.append(row)


# Write function to calculate great circle distance
def great_circle_distance(latitudeA, longitudeA, latitudeB, longitudeB):

    # Convert to radians
    latitudeA = math.radians(latitudeA)
    longitudeA = math.radians(longitudeA)
    latitudeB = math.radians(latitudeB)
    longitudeB = math.radians(longitudeB)

    # Calculate the distance
    distance = math.acos((math.sin(latitudeA) * math.sin(latitudeB)) +
                         (math.cos(latitudeA)*math.cos(latitudeB) *
                          math.cos(longitudeA-longitudeB)))
    totalDistance = distance * 6300

    return round(totalDistance)


print("This program takes two cities in the data and calculates the great\
      circle distance between them.")

# Ask for city A name
city_input_a = input("Enter the first city name. ")

# Assume city A not found as default
city_a = None

for row in city_data:

    # Check if city A is found
    if city_input_a == row['label']:

        # Change city A to found
        city_a = row

# If city name not found, announce fail
if not city_a:
    print("City name not found in the data.")

# If city A found, continue
if city_a:

    # Ask for city B
    city_input_b = input("Enter the second city name. ")

    # Assume city B not found as default
    city_b = None

    for row in city_data:

        # Check if city B is found
        if city_input_b == row['label']:

            # Change city B to found
            city_b = row

    # If both city A and city B are found, calculate distance
    if city_a and city_b:

        distance = great_circle_distance(
            float(city_a['latitude']),
            float(city_a['longitude']),
            float(city_b['latitude']),
            float(city_b['longitude'])
        )

        # Prints result
        print("The distance between", city_input_a, "and", city_input_b,
              "is", distance, "km.")

    # If city B not found, announce fail
    if not city_b:
        print("City name not found in the data.")
