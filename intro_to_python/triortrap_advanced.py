# This program calculates the area of a triangle or trapezoid.

# Says what the program will help the user do, followed by an empty line
print("This program finds the area of a triangle or a trapezoid.")
print()

# Asks the user which type of shape will be used in the program
shape = input("Are you calculating the area of a triangle or trapezoid? ")

# Determines if the user is calculating the area of a triangle and follows the triangle program
if shape == 'triangle':

    loopCount = 0

    # The "while" statement keeps looping until its condition (loopCount<4) made False.
    while loopCount < 4:
        
        # loopCount will increase 1 for each loop
        loopCount += 1

        # Attempts to convert inputs to floats
        try:
            # Asks the user for the measurements of the triangle, converts those numbers to float, and defines them as two separate variables
            height = float(input("Please enter the height of the triangle: "))
            base = float(input("Please enter the base length of the triangle: "))

            # Defines the variable area as the calculation of a triangle area from the inputs
            area = 0.5 * height * base

            # Says what the results of the program are while restating the user's inputs
            print("The area of a triangle with height", height, "and base", base, "is", area, ".")
            break

        except:
            # Asks the user to re-enter inputs if they cannot be converted to float
            if loopCount < 4:
                print('\nYou did not enter a number. Please re-enter your measurements.')

            # Tells user the program has failed after too many attempts
            if loopCount == 4:
                print('\nYou have failed to enter a number too many times. Program failed.')
    
# Determines if the user is calculating the area of a trapezoid and follows the trapezoid program
elif shape == 'trapezoid':
    
    loopCount = 0

    # The "while" statement keeps looping until its condition (loopCount<4) made False.
    while loopCount < 4:
        
        # loopCount will increase 1 for each loop
        loopCount += 1

        #Attempts to convert inputs to floats
        try:
            # Asks the user for the measurements of the trapezoid, converts those numbers to float, and defines them as two separate variables
            height = float(input("Please enter the height of the trapezoid: "))
            low_base = float(input("Please enter the bottom base length of the trapezoid: "))
            up_base = float(input("Please enter the top base length of the trapezoid: "))

            # Defines the variable area as the calculation of a trapezoidal area from the inputs
            area = 0.5 * (low_base + up_base) * height

            # Says what the results of the program are while restating the user's inputs
            print("The area of a trapezoid with height", height, "bottom base", low_base, "upper base", up_base, "is", area, ".")
            break

        except:
            # Asks the user to re-enter inputs if they cannot be converted to float
            if loopCount < 4:
                print('\nYou did not enter a number. Please re-enter your measurements.')

            # Tells user the program has failed after too many attempts
            if loopCount == 4:
                print('\nYou have failed to enter a number too many times. Program failed.')
    
# Checks if neither triangle nor trapezoid was chosen and prevents the program from doing any calculations
else:
    print("This program only calculates the area of a triangle or trapezoid.")
