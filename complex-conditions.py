
# Practice from Week 03 CSE 110 - Learning Complex Conditions
# by Adson Mettler

print()
print('Please, rate on the following questions from 1-10:')
loan_size = int(input('\nHow large is the loan? '))
credit_history = int(input('How good is your credit history? '))
income = int(input('How high is your income? '))
down_payment = int(input('How large is your down paymento? '))
print()

should_loan = False

if loan_size >= 5:
    if credit_history >= 7 and income >= 7:
        should_loan = True
    elif credit_history >= 7 or income >= 7:
        if down_payment >= 5:
            should_loan = True
        else:
            should_loan = False

if loan_size < 5:
    if credit_history < 4:
        should_loan = False
    elif income >= 7 or down_payment >= 7:
        should_loan = True
    elif income >= 4 and down_payment >= 4:
        should_loan = True
    else:
        should_loan = False

if should_loan:
    print('Yes, you got the loan!')
else:
    print("I'm sorry, you didn't get the loan!")
print()

