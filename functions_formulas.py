
## This is a practice for creating formulas using FUNCTIONS ##
# Author: Adson Mettler do Nascimento

import math

# Function to calculate area of a square
def compute_area_square(side):
    return side * side

# Function to calculate area of a rectangle
def compute_area_rectangle(length, width):
    return length * width

# Function to calculate area of a circle
def compute_area_circle(radius):
    return math.pi * radius**2


shape_list = ["Square", "Rectangle", "Circle", "Quit"]

print("\nWELCOME TO ADSON's CALCULATOR")
print("==================================")

shape = ""

while shape != "4":
    print("\nHere are the shapes you can calculate?")
    for i, menu_item in enumerate(shape_list):
        print(f"{i + 1}. {menu_item}.")
    
    shape = input("\nPlease, type the number related to the shape you want to calculate: ")

    if shape == "1":
        side = float(input("Type the number of the square lengh: "))
        area = compute_area_square(side)
        print(f"The area of your square is: {area:.2f}")

    elif shape == "2":
        length = float(input("Type one of the length of the rectangle: "))
        width = float(input("Type the width of the rectangle: "))
        area = compute_area_rectangle(length, width)
        print(f"The area of your rectangle is: {area:.2f}")
            
    elif shape == "3":
        radius = float(input("Type the radius of the circle: "))
        area = compute_area_circle(radius)
        print(f"The area of your circle is: {area:.2f}")

    elif shape == "4":
        print("\nThank you for using my program!")
        print("Hope to see you soon!")
        print("Bye!!!\n")
        break

    else:
        print("\n*********************************************")
        print("Invalid menu option! Please, try again!")
        print("*********************************************")
        print()
