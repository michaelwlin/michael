
# CIS 41A Lab - 2 Income Tax Calculator
# Description: Takes an income and calculates how much income tax should be paid
# By Michael Lin

# Set some variables for Income Brackets
b1 = {
    "tax": 0.01,
    "limit": 50000
}
b2 = {
    "tax": 0.02,
    "limit": 75000
}
b3 = {
    "tax": 0.03,
    "limit": 100000
}
b4 = {
    "tax": 0.04,
    "limit": 250000
}
b5 = {
    "tax": 0.05,
    "limit": 500000
}
b6 = {
    "tax": 0.06,
    "limit": None
}
# Set initial variable for income_tax
income_tax = 0

# While loop to ensure the user inputs a valid number (float/integer & > 0)
while True:
    try:
        # Take user input then convert it to float 
        # It will have a ValueError error if not a valid number & the except will catch that
        income = (input("Please enter gross income: $"))
        temp = float(income)
        
        # Check edge case (< 0)
        if temp < 0:
            print("Please enter a positive value.")

        # Check first case
        elif temp < b1['limit']:
            income_tax = (temp*b1['tax'])
            break

        # Now check other cases 
        elif temp < b2['limit']:
            income_tax = ((b1['limit']*b1['tax']) + ((temp-b1['limit'])*b2['tax']))
            break

        elif temp < b3['limit']:
            income_tax = ((b1['limit']*b1['tax']) + ((b2['limit']-b1['limit'])*b2['tax']) + 
            ((temp-b2['limit'])*b3['tax'])) 
            break

        elif temp < b4['limit']:
            income_tax = ((b1['limit']*b1['tax']) + ((b2['limit']-b1['limit'])*b2['tax']) + 
            ((b3['limit']-b2['limit'])*b3['tax']) + ((temp-b3['limit'])*b4['tax'])) 
            break
            
        elif temp < b5['limit']:
            income_tax = ((b1['limit']*b1['tax']) + ((b2['limit']-b1['limit'])*b2['tax']) + 
            ((b3['limit']-b2['limit'])*b3['tax']) + ((b4['limit']-b3['limit'])*b4['tax']) +
            ((temp-b4['limit'])*b5['tax']))
            break

        # Last case is if income is > Bracket 5 Limit
        else:
            income_tax = ((b1['limit']*b1['tax']) + ((b2['limit']-b1['limit'])*b2['tax']) + 
            ((b3['limit']-b2['limit'])*b3['tax']) + ((b4['limit']-b3['limit'])*b4['tax']) +
            ((b5['limit']-b4['limit'])*b5['tax']) + ((temp-b5['limit'])*b6['tax']))
            break

    # This will catch the ValueError if the user does not input the specified types
    except ValueError:
        print("Please enter a valid number!")

# Print out the calculation!
print('Tax due: $%.2f' %(income_tax))

"""
The following is the record of program execution and outputs:

Please enter gross income: $25000
Tax due: $250.00

Please enter gross income: $74999
Tax due: $999.98

Please enter gross income: $100050
Tax due: $1752.00

Please enter gross income: $450500
Tax due: $17775.00

Please enter gross income: $1000000
Tax due: $50250.00
"""

