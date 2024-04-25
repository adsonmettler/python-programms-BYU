
# Activity 2 - Data in files practice

# Author: Adson Mettler do Nascimento

people = [
    "Stephanie 36",
    "John 29",
    "Emily 24",
    "Gretchen 54",
    "Noah 12",
    "Penelope 32",
    "Michael 2",
    "Jacob 10"
]

        # the logic here is puting the largest number in the variable "youngest" to make the loop read from the
        # biggest number until the smaller, so we get the smaller number. And when we want to get the biggest
        # number we have to start the variable from the smallest number possible, to make the loop read from
        # the smaller until the biggest number.
youngest = 99999
youngest_name = ""

for line in people:
    line = line.split()
    print(line)

    name = line[0]
    age = int(line[1])

    if age < youngest:

        youngest = age

        youngest_name = name

print(f"The youngest person is: {youngest_name}, {youngest} years old.")

