numbers = []
number = ''
largest = -999999
smallest = 999999

while number != 0:
    
    number = input('Please enter a number. To finish, enter 0: ')
    try:
        number = int(number)
        numbers.append(number)
        if number > largest and number != 0:
            largest = number
        if number < smallest and number > 0:
            smallest = number
    except ValueError:
        print('You must enter a number. ')

total = sum(numbers)
print(f'Sum of all numbers: {total}')

average = int(total) / len(numbers)
print(f'The average is {average:.3f}')

print(f"The largest number is {largest}")
print(f"The smallest positive number is {smallest}")

sorted_list = sorted(numbers)
print('The sorted list:')
print(sorted_list, end='')
print()