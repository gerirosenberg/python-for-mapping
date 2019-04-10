# Reads CityPop, stores it in dictionaries, finds the population of a city
# at a specific year

import csv
import os.path

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

# Ask for city name
city_input = input("Enter the city name. ")

# Assume city not found as default
city_found = False

for row in city_data:

    # If city input matches a city in a dictionary, continue asking for input
    if city_input == row['label']:
        yr_input = input("Enter the year. ")
        yr_input = 'yr' + yr_input

        # Change city to found
        city_found = True

        # If year input doesn't match a dictionary key, announce fail
        if yr_input not in row:
            print("Year not in data.")

        # If year input matches a dictionary key, print result
        if yr_input in row:
            print("The population in", yr_input, "was",
                  row[yr_input], "million.")

# If city still not found, announce fail
if not city_found:
    print("City name not found in data.")
