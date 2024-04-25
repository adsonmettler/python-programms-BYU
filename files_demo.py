
# Practice activity - opening and reading files
# Author: Adson Mettler do Nascimento

with open("courses.txt") as courses_file:
    for line in courses_file:
        # line = "CSE 110,98.5"
        line = line.strip()

        parts = line.split(",")
        # parts = ["CSE 110", "98.5"]

        name = parts[0]
        grade = float(parts[1])

        bonus_grade = grade + 3

        print(f"{name} - Grade: {grade}, after bonus: {bonus_grade}")


    print(courses_file)

print("The file is closed now!")