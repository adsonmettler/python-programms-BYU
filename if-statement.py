# FOLLOWING THE VIDEO CLASS 1

# country = input('What country do you live in? ')
# tax = 0

# if country.lower() == 'canada':
#     province = input('What province do you live? ')
#     if province.lower() in('alberta', 'nunavut', 'yukon'):
#         tax = 0.05
#     elif province.lower() == 'ontario':
#         tax = 0.13
#     else:
#         tax = 0.15
# print(tax)


# ACTIVITY 1

print()
first_number = int(input('What is the first number? '))
second_number = int(input('What is the second number? '))
if first_number > second_number:
    print('The first number is greater')
else:
    print('The first number is not greater')

if first_number == second_number:
    print('The numbers are equal')
else:
    print('The numbers are not equal')

if first_number < second_number:
    print('Second number is greater')
else:
    print('The second number is not greater')

print()

user_animal = input('What is your favorite animal? ')
if user_animal.lower() == 'dog':
    print("That's my favorite too!")
else:
    print("That one is not my favorite.")


# FOLLOWING THE VIDEO CLASS 2

gpa = float(input("What was your Grade Point Average? "))
lowest_grade = float(input('What was your lowest grade? '))

if gpa >= 0.85 and lowest_grade >= 0.70:
    honour_roll = True
else:
    honour_roll = False

if honour_roll:
    print('You made honour roll')

