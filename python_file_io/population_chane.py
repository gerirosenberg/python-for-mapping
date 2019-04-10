# Reads CityPop, stores it in dictionaries, prompts the user for two years,
# and writes a new csv with the population difference for every city
# between those two years

import csv
import os.path


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


# Get input from user and determine if it is valid
def get_value_from_user(prompt, value_check, error_message):

    while True:
        # Get input from user
        user_input = 'yr' + input(prompt)

        # Restart function if input not in data
        if user_input not in value_check:
            print(error_message)
            continue

        # Continue if input is in data
        else:
            return user_input


# Calculate population change
def calculate_population_change(yr_a, yr_b):

    # Calculate the difference in population
    difference = float(yr_b) - float(yr_a)

    return round(difference, 2)


# Write data into new csv file
def write_csv_file(name_of_file, data_for_file):

    # Open a connection to a new file and prepare to write into it
    with open(name_of_file, 'w') as f:

        # Create the CSV writing tool
        writer = csv.DictWriter(
            f, fieldnames=('id', 'label', 'population_change'),
            extrasaction='ignore'
            )

        # CSV tool writes the first row with only the header names
        writer.writeheader()

        # Add a new line for each city
        for row in data_for_file:
            writer.writerow(row)


if __name__ == '__main__':
    data = read_csv_file('CityPop.csv')

    # Announce what program does
    print("This program takes two years and calculates the population change\
      for all cities in the data and stores it in CityPopChg.csv.")

    # Make blank list for available_years
    available_years = []

    # Select only keys that are years
    for item in data[0].keys():
        if item.startswith('yr'):

            # Write keys to avaiable_years list
            available_years.append(item)

    # Get values for each year from user
    year_1 = get_value_from_user('Enter the first year ', available_years,
                                 'Year not in data.')
    year_2 = get_value_from_user('Enter the second year ', available_years,
                                 'Year not in data.')

    # Create new list for population change
    population_change_data = []

    for row in data:

        # Calculate population change
        population_change = calculate_population_change(
            row[year_1], row[year_2]
            )

        # Get all desired values for new CSV
        pop_chg_info = {
            'id': row['id'],
            'label': row['label'],
            'population_change': population_change
        }

        # Get all desired values for new CSV
        population_change_data.append(pop_chg_info)

    # Write results into new csv
    write_csv_file('CityPopChg.csv', population_change_data)
