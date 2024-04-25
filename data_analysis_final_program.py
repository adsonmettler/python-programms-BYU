
## DATA ANALYSIS PROGRAM ##

# Author: Adson Mettler do Nascimento

### EXCEEDING ACTIVITY ###
# I added an user country input to show the minimum and maximum average
# of life expectancy for that country.

print("\n\nWelcome to Life Expectancy Data Analysis Table!")
print("==========================================================")
print()
print("On this dataset you can drive through from 1751 until 2019,")
print("and chose an year or country to see have a return of the")
print("average of life expectancy in each time or country in the")
print("world.")
print()
print("I hope you enjoy to find some interesting data on your analysis.")

total_expectancy = 0
line_count = -1

with open("life-expectancy.csv") as life_expectancy_file:

    year_of_interest = int(input("\nEnter the year of interest: "))

    max_expectancy = 0
    min_expectancy = 999999
    country_max = ""
    country_min = ""
    year_max = ""
    year_min = ""

    for line in life_expectancy_file:
        line = line.strip()
        parts = line.split(",")
        
        country_name = parts[0]
        year = parts[2]
        expectancy = parts[3]
        
        try:
            year = int(year)
            expectancy = float(expectancy)
        except ValueError:
            continue

        if expectancy > max_expectancy:
            max_expectancy = expectancy
            country_max = country_name
            year_max = year
            
        elif expectancy < min_expectancy:
            min_expectancy = expectancy
            country_min = country_name
            year_min = year

print(f"\nThe overall max life expectancy is {max_expectancy} from {country_max} in {year_max}.")
print(f"The overall min life expectancy is {min_expectancy} from {country_min} in {year_min}.\n")

with open("life-expectancy.csv") as life_expectancy_file:

    max_expectancy = 0
    min_expectancy = 999999
    country_max = ""
    country_min = ""
    year_max = ""
    year_min = ""

    total_expectancy = 0
    line_count = -1

    for line in life_expectancy_file:
        line = line.strip()
        parts = line.split(",")

        country_name = parts[0]
        year = parts[2]
        expectancy = parts[3]
            
        try:
            year = int(year)
            expectancy = float(expectancy)
        except ValueError:
            continue

        total_expectancy += expectancy
        line_count += 1

    average_expectancy = total_expectancy / line_count

print(f"For the year {year_of_interest}:")
print(f"The average life expectancy across all countries was {average_expectancy:.2f}")

with open("life-expectancy.csv") as life_expectancy_file:

    max_expectancy = 0
    min_expectancy = 999999
    country_max = ""
    country_min = ""
    year_max = ""
    year_min = ""


    for line in life_expectancy_file:
        line = line.strip()
        parts = line.split(",")

        country_name = parts[0]
        year = parts[2]
        expectancy = parts[3]
            
        try:
            year = int(year)
            expectancy = float(expectancy)
        except ValueError:
            continue
                
        if year == year_of_interest and expectancy > max_expectancy:
            max_expectancy = expectancy
            country_max = country_name

        if year == year_of_interest and expectancy < min_expectancy:
            min_expectancy = expectancy
            country_min = country_name

print(f"The max life expectancy was in {country_max} with {max_expectancy}")
print(f"The min life expectancy was in {country_min} with {min_expectancy}\n")


with open("life-expectancy.csv") as life_expectancy_file:

    country_of_interest = (input("\nEnter the country of interest: ")).lower()

    max_expectancy = 0
    min_expectancy = 999999
    country_max = ""
    country_min = ""
    year_max = ""
    year_min = ""

    for line in life_expectancy_file:
        line = line.strip()
        parts = line.split(",")
        
        country_name = parts[0].lower()
        year = parts[2]
        expectancy = parts[3]
        
        try:
            year = int(year)
            expectancy = float(expectancy)
        except ValueError:
            continue

        country_name = country_name

        if country_name == country_of_interest and expectancy > max_expectancy:
            max_expectancy = expectancy
            country_max = country_name

        if country_name == country_of_interest and expectancy < min_expectancy:
            min_expectancy = expectancy
            country_min = country_name

    if country_max and country_min:
        print(f"\nFor the country {country_of_interest.title()}:")
        print(f"The max life expectancy was {max_expectancy}")
        print(f"The min life expectancy was {min_expectancy}\n")

    else:
        print("I am sorry, invalid input. Please, try again!")

