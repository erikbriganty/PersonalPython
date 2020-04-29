# File name: stadium.py
# Name: Erik Briganty
# Date: 04/07/2020


# Stadium Seating

# Defining the price per ticket
costA = 15
costB = 12
costC = 9

# Welcome Message
print('\nWelcome to the Broward College Stadium!\n')

# Asking user to input number of tickets sold
ticketA = int(input('How many Class A tickets were sold? '))
ticketB = int(input('How many Class B tickets were sold? '))
ticketC = int(input('How many Class C tickets were sold? '))

# Calculating total number of tickets sold
totalSold = ticketA + ticketB + ticketC

# Displaying total number of tickets sold
print('\n**********************')
print('Total number of tickets sold:', totalSold)

# Calculating income generated for each class of tickets
# Calculating total income generated
incomeA = ticketA * costA
incomeB = ticketB * costB
incomeC = ticketC * costC
totalIncome = incomeA + incomeB + incomeC

# Displaying income generated
# Formatted variables for dollar sign, comma, and two decimal places
print('\nIncome Generated:')
print('Class A: ${:,.2f}' .format(incomeA))
print('Class B: ${:,.2f}' .format(incomeB))
print('Class C: ${:,.2f}' .format(incomeC))
print('Total Income: ${:,.2f}' .format(totalIncome))
