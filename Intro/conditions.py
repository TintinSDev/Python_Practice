price = 1000000
good_credit = True

if good_credit:
    down_payment = 0.1 * price
else:
    down_payment = 0.2 * price
print(f'Down Payment: ${down_payment}')
# LOGICAL OPERATORS
#and = both are true
#or = at least one
#not =
income = True
credit = False
if income and credit:
    print ('Eligible')
# comparison operators ><=

name = 'Martin'

if len(name) < 3:
    print('Name must be at least 3 characters long')
elif len(name) > 50:
    print('Name can be a maximum of 50 characters')
else:
    print('name looks good')

