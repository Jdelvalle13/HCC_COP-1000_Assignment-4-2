"""
This program calculates an employee's productivity bonus and prints the employee's name and bonus
"""


# Validates input data is valid
def checkInput(shiftsString, transactionsString, dollarValueString):


    # Check if numCharsString is numeric and positive
    if not shiftsString.isdigit():
        return 'Invalid number of shifts entered. Please enter a positive number.'
    shifts = int(shiftsString)
    if shifts < 0:
        return 'Invalid number of shifts entered. Please enter a positive number.'
    

    # Check if transactionsString is numeric and positive
    if not transactionsString.isdigit():
        return 'Invalid number of transactions entered. Please enter a positive number.'
    transactions = int(transactionsString)    
    if transactions < 0:
        return 'Invalid number of transactions entered. Please enter a positive number.'
    

    # Check if dollarValueString is numeric and positive
    if not dollarValueString.isdigit():
        return 'Invalid transaction value entered.  Please enter a positive number.'
    dollarValue = int(dollarValueString)
    if dollarValue < 0:
        return 'Invalid transaction value entered.  Please enter a positive number.'
    

    # Final return of checkInput
    return 'valid'


# User Inputs
employeeNameString = input("Please enter the employee's name: ")
shiftsString = input("Please enter number of shifts worked: ")
transactionsString = input("Please enter number of transactions: ")
dollarValueString = input("Please enter transaction dollar value: ")


# Validation result of user iput using checkInput()
validationResult = checkInput(shiftsString, transactionsString,dollarValueString)

# If validation fails, stop the program and print error message
if validationResult != 'valid':
    print(validationResult)
else:
    # Employee's Name
    employeeName = employeeNameString
    
    # Number of shifts worked
    shifts = int(shiftsString)
    
    # Number of transactions made
    transactions = int(transactionsString)
    
    # Dollar Value of transactions
    dollarValue = float(dollarValueString) + 0.00
    
    
    # Calculated productivity score:
    # Dollar value of transactions divided by number transactions all divided by number of shifts
    productivityScore = int((dollarValue / transactions) / shifts)

    # Bonus Ranges and amounts
    bonusRange1 = 30
    bonusRange2 = 69
    bonusRange3 = 199
    bonus1 = 50
    bonus2 = 75
    bonus3 = 100
    bonus4 = 200


    # Calculated bonuses base on productivity Score
    if productivityScore <= bonusRange1:
        bonus = bonus1
    elif productivityScore <= bonusRange2:
        bonus = bonus2
    elif productivityScore <= bonusRange3:
        bonus = bonus3
    else:
        bonus = bonus4
        

    # Output results
    print(f"Employee's Name: {employeeName}")
    print(f"Employee Bonus: ${bonus:.2f}")