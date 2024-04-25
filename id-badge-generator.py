# Id Badge Generator
# created by Adson

print('\nPlease enter the following information:\n')
first_name = input('First Name: ')
last_name = input('Last Name: ')
email_address = input('Email Address: ')
phone_number = input('Phone Number: ')
job_title = input('Job Title: ')
id_number = input('ID Number: ')

# output = f'\nThe ID Card is: \n-----------------------\n{last_name.upper()}, {first_name.title()}\n{job_title.title()}\nID: {id_number}\n \n{email_address.lower()}\n{phone_number}\n-----------------------'
# print(output)

print('\nThe ID Card is:')
print('-------------------------')
print(f'{last_name.upper()}, {first_name.title()}')
print(job_title.title())
print()
print(email_address.lower())
print(phone_number)
print('-------------------------')