# This program calculates the area of a triangle.

# Says what the program will help the user do, followed by an empty line
print("This program finds the area of a triangle.")
print()

# Asks the user for the measurements of the triangle, converts those numbers to float, and defines them as two separate variables
height = float(input("Please enter the height of the triangle: "))
base = float(input("Please enter the base length of the triangle: "))

# Defines the variable area as the multiplication of the user's inputs by 0.5
area = 0.5 * height * base

# Says what the results of the program are while restating the user's inputs
print("The area of a triangle with height", height, "and base", base, "is", area, ".")
