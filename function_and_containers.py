# This code takes an input latitude or longitude in DD or DMS format,
# announces which format is in in, and converts it to the other format.


# DMS to DD function
def convert_dms_to_dd(dms_input):

    degrees, minutes, seconds = dms_input

    # If degreee is positive
    if 0 <= degrees <= 180:

        # Convert DMS to DD
        dd = degrees + (minutes/60) + (seconds/3600)

    # If degree is negative
    if -180 <= degrees < 0:

        # Convert DMS to DD
        dd = degrees - (minutes/60) - (seconds/3600)

    return dd


# DD to DMS function
def convert_dd_to_dms(dd_input):

    degrees = int(dd_input)

    # Convert DD to DMS
    minutes = int((abs(dd_input) - abs(degrees)) * 60)
    seconds = (abs(dd_input) - abs(degrees) - abs(minutes/60)) * 3600

    return (degrees, minutes, seconds)


while True:

    # Ask for input coordinate
    user_input = input("Enter a longitude or latitude in DMS or DD format. ")

    # Exit if no choice entered
    if not user_input:
        break

    # Split coordinate into a tuple and covnert to floats
    coord = user_input.split(',')

    if len(coord) >= 1:

        try:
            coord[0] = float(coord[0])

        # If a non-number is entered, assume error
        except ValueError:
            print("The input is not a number. Please try again.")
            continue

    if len(coord) >= 2:
        coord[1] = float(coord[1])

    if len(coord) == 3:
        coord[2] = float(coord[2])

    if not -180 <= coord[0] <= 180:
        print("The degrees are out range. Please try again.")
        continue

    # If the tuple has only one object, assume DD and convert
    if len(coord) == 1:

        # Assign coordinate to new variable for function
        dd_input = coord[0]

        # Display conversion result
        print("The input is in DD format.")
        print("Its DMS form is ", convert_dd_to_dms(dd_input))
        break

    # If the tuple has only two objects, assume error
    if len(coord) == 2:
        print("The input is not in a correct format. Please try again.")
        continue

    # If minutes are out of range, assume error
    if not 0 <= coord[1] < 60:
        print("The minutes are out of range. Please try again.")
        continue

    # If seconds are out of range, assume error
    if not 0 <= coord[2] < 3600:
        print("The seconds are out of range. Please try again.")
        continue

    # If 3 variables in correct range, assume DMS and convert
    if len(coord) == 3:

        # Assign variables for DMS format
        degrees = coord[0]
        minutes = coord[1]
        seconds = coord[2]

        # Display conversion result
        print("The input is in DMS format.")
        print("Its DD form is ",
              convert_dms_to_dd((degrees, minutes, seconds)))
        break
