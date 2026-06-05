
# Get details of loan
money_owed = float(input('How much money do you owe, in dollars?\n')) # ex $50,000
apr = float(input('What is the annual percentage rate of the loan?\n')) # ex 3%
payment = float(input('How much will you pay off each month in dollars?\n')) # ex $1000
months = int(input('How many months do you want to see the results for?\n')) # ex 24

monthly_rate = apr/100/12

for i in range(months):
    # Calculate interest to pay
    interest_paid = money_owed * monthly_rate

    # Add in interest
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print('The last payment is', money_owed)
        print('You paid off the loan in', i+1, 'months')
        break

    # Make payment
    money_owed = money_owed - payment 

    # end here denotes that instead of the usual nl sep at the end, we add a space, 
    # replacing the nl with a space, meaning both lines are printed on the same line
    print('Paid', payment, 'of which', interest_paid, 'was interest,', end = ' ')
    print('Now I owe', money_owed)