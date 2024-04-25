
### WIND CHILL CALCULATOR ###
# Author: Adson Mettler do Nascimento

import math

# Function to calculate and return the wind chill based on temperature and wind speed.
def calculate_wind_chill(fahrenheit, wind_speed):
    wind_chill = 35.74 + (0.6215 * fahrenheit) - (35.75 * wind_speed ** 0.16) + (0.4275 * fahrenheit * wind_speed ** 0.16)
    return wind_chill

# Function to convert celsius into fahrenheit.
def convert_celsius_to_fahrenheit(celsius):
    fahrenheit = (celsius * 9 / 5) + 32
    return fahrenheit


while True:
    temperature = float(input("\nWhat is the temperature? "))
    unit = input("Fahrenheit or Celsius? Type F or C: ").upper()

    if unit == "C":
        temperature = convert_celsius_to_fahrenheit(temperature)

    print(f"At temperature {temperature:.1f}F:")
    for wind_speed in range(5, 61, 5):
        wind_chill = calculate_wind_chill(temperature, wind_speed)
        print(f"At wind speed {wind_speed} mph, the wind chill is: {wind_chill:.2f}F")
    print()

    # if temperature != float():
    #     print("Thank you for using Wind Chill Calculator, bye!\n")
    #     break

