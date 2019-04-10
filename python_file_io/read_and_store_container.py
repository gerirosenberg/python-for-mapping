# Reads CityPop and stores it in dictionaries

import csv
import os.path

filename = 'CityPop.csv'

# If filename is bad, tell the user
if not os.path.isfile(filename):
    print("File does not exist.")

# Open CityPop using DictReader, which stores each row as a dictionary
with open(filename, 'r') as f:
    csv_reader = csv.DictReader(f)
