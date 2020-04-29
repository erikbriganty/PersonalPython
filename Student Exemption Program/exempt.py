# File name: exempt.py
# Name: Erik Briganty
# Date: 04/07/2020

# Program Introduction
print('Welcome to the Millionaire Game Exemption Program!\n')

# Defining average
average = None

# Prompt user for average, repeat prompt if value is not correct
while True:
    try:
        average = int(input('Enter the students average: '))
    except ValueError:
        print('Sorry, please enter a valid number.')
        # Try again
        continue
    if average > 100:
        print('Invalid. Average must be between 0 and 100.')
        continue
    elif average < 0:
        print('Invalid. Average must be between 0 and 100.')
        continue
    else:
        # Successful input
        break

# Defining days_missed
days_missed = None

# Prompt user for number of days missed, repeat prompt if value is not correct
while True:
    try:
        days_missed = int(input('Enter number of days absent: '))
    except ValueError:
        print('Sorry, please enter a valid number.')
        # Try again
        continue
    if days_missed < 0:
        print('Invalid. Number of days missed can not be less than 0.')
    elif days_missed > 30:
        print('Invalid. Number of days missed can not be greater than 30.')
    else:
        # Successful input
        break

# Display if the student is exempt or not exempt
if average >= 96:
    print('Congratulations! You are exempt from the final because your average is a 96 or better!')
elif average >= 93 and days_missed < 3:
    print('Congratulations! You are exempt because your average is at least a 93 and missed less than 3 days.')
elif average >= 90 and days_missed == 0:
    print('Congratulations! You are exempt because your average is at least a 90 and have perfect attendance.')
else:
    print('Sorry, you are not exempt.')
