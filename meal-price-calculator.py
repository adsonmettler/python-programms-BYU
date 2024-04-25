# Meal Price Calculator
# by Adson Mettler do Nascimento

# EXCEEDING:
# I added to my program drink and dessert price, 
# and I added a tip percentage for the service to add in the total price.

print("\nPlease, filled up the form below: ")
child_meal = float(input("\nWhat is the price of a child's meal? "))
child_drink = float(input("What is the price of a child's drink? "))
child_dessert = float(input("What is the price of a child's dessert? "))
adult_meal = float(input("What is the price of an adult's meal? "))
adult_drink = float(input("What is the price of an adult's drink? "))
adult_dessert = float(input("What is the price of adult's dessert? "))
how_many_child = int(input("How many children are there? "))
how_many_adults = int(input("How many adults are there? "))
subtotal = float(((child_meal + child_drink + child_dessert) * how_many_child) + ((adult_meal + adult_drink + adult_dessert) * how_many_adults))

print(f'\nSubtotal: ${subtotal:.2f}')

tax_rate = float(input("\nWhat is the sales tax rate? "))
tip_rate = float(input('What is the percentage of tips you would give? '))
sales_tax = float((subtotal * tax_rate) / 100)
tip_amount = float((subtotal * tip_rate) / 100)
print(f'Sales Tax: ${sales_tax:.2f}')
print(f'Tip Amount: ${tip_amount:.2f}')
print(f'Total: ${subtotal + sales_tax:.2f}')

payment_amount = float(input('\nWhat is the payment amount? '))
total = float(subtotal + sales_tax)
change = float(payment_amount - total)
print(f'Change: ${change:.2f}')
print()