
# Author: Adson Mettler do Nascimento
# WHILE LOOP with numbers ###

# positive_number = int(input('Please, type a positive number: '))

# while positive_number < 0:
#     print('Sorry, this is not a positive number!')
#     positive_number = int(input('Please, type a positive number: '))

# print(f"The number is: {positive_number}")


# WHILE LOOP with strings ###

candy = input('May I have a piece of candy? ')

while not candy.lower() == 'yes':
    candy = input('May I have a piece of candy? ')

print("Thank you!")

# INSTRUCTOR version ###

candy = ""

while candy.lower() != 'yes':
    candy = input('May I have a piece of candy? ')

print("Thank you!")