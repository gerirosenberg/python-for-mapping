# Reads CityPop, converts data to City class, stores in list,
# and prints resulting data

import csv
import os.path
import math


# Open and read csv file
def read_csv_file(filename):

    # If filename is bad, tell the user
    if not os.path.isfile(filename):
        print("File does not exist.")

    # Make data into list
    datalist = []

    # Open CityPop using DictReader, which stores each row as a dictionary
    with open(filename, 'r') as f:
        reader = csv.DictReader(f)

        # Make each row into a separate dictionary
        for row in reader:
            datalist.append(row)

    return datalist


# Creates new class for cities
class City(object):
    def __init__(
        self, Name, Label, Lat, Lon, Pop1970, Pop1975,
            Pop1980, Pop1985, Pop1990, Pop1995, Pop2000, Pop2005,
            Pop2010):

        # Define parameters
        self.city = Name
        self.label = Label

        Lat = float(Lat)
        if Lat > 90 or Lat < -90:
            print("The value of latitude is not valid.")
        else:
            self.lat = Lat

        Lon = float(Lon)
        if Lon > 180 or Lon < -180:
            print("The value of longitude is not valid.")
        else:
            self.lon = Lon

        self.pop1970 = float(Pop1970)
        self.pop1975 = float(Pop1975)
        self.pop1980 = float(Pop1980)
        self.pop1985 = float(Pop1985)
        self.pop1990 = float(Pop1990)
        self.pop1995 = float(Pop1995)
        self.pop2000 = float(Pop2000)
        self.pop2005 = float(Pop2005)
        self.pop2010 = float(Pop2010)

    # This defines what city_data will look like when printed
    def __repr__(self):
        return "<City object " + self.city + ", " + self.label + ", " +\
                 str(self.lat) + ", " + str(self.lon) + ", " +\
                 str(self.pop1970) + ", " + str(self.pop1975) + ", " +\
                 str(self.pop1980) + ", " + str(self.pop1985) + ", " +\
                 str(self.pop1990) + ", " + str(self.pop1995) + ", " +\
                 str(self.pop2000) + ", " + str(self.pop2005) + ", " +\
                 str(self.pop2010) + ">"

    # Function to print distance between two cities
    def printDistance(self, othercity):

        # Convert to radians
        latitudeA = math.radians(self.lat)
        longitudeA = math.radians(self.lon)
        latitudeB = math.radians(othercity.lat)
        longitudeB = math.radians(othercity.lon)

        # Calculate the distance
        distance = math.acos((math.sin(latitudeA) * math.sin(latitudeB)) +
                             (math.cos(latitudeA)*math.cos(latitudeB) *
                              math.cos(longitudeA-longitudeB)))
        totalDistance = distance * 6300

        # Print results
        format = '%s is %.1f km from %s.'
        values = (self.label, totalDistance, othercity.label)
        print(format % values)

    # Function to print population change for one city between two years
    def printPopChange(self, year1, year2):
        # Add "pop" to year
        year1_pop = "pop" + str(year1)
        year2_pop = "pop" + str(year2)

        # Calculate the difference in population
        difference = getattr(self, year2_pop) - getattr(self, year1_pop)

        # Print results
        format = 'The population change for %s between %s and %s is %.2f million people.'
        values = (self.label, year1, year2, difference)
        print(format % values)


# Stores data into classes in list
def fill_cities_with_classes(data):
    # Create new blank list for storing
    cities = []

    # Loop through each row in data
    for row in data:

        # Assign each parameter to a value from the data
        city = City(
            Name=row['city'], Label=row['label'], Lat=row['latitude'],
            Lon=row['longitude'], Pop1970=row['yr1970'],
            Pop1975=row['yr1975'], Pop1980=row['yr1980'],
            Pop1985=row['yr1985'], Pop1990=row['yr1990'],
            Pop1995=row['yr1995'], Pop2000=row['yr2000'],
            Pop2005=row['yr2005'], Pop2010=row['yr2010']
            )

        # Add to list
        cities.append(city)

    # Return now filled list
    return cities


if __name__ == '__main__':
    # Opens and reads file
    data = read_csv_file('CityPop.csv')

    # Announce what program does
    print("This program takes CityPop.csv and stores it into a class, City.")

    # Store data into classes in list
    city_data = fill_cities_with_classes(data)

    # Print out all attributes
    print(city_data)

    # Test out class methods
    city_data[0].printDistance(city_data[1])
    city_data[0].printPopChange(1970, 1990)
