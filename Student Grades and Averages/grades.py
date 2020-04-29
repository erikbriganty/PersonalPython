# File name: grades.py
# Name: Erik Briganty
# Date: 04/24/20


import re
from statistics import mean


def file_info():

    # Open & read file
    grades_file = open('grades.txt', 'r')
    file_contents = grades_file.read()

    # Print Header & spacer
    print('Name' + '\t\tGrade')
    print('---------------------')

    # Print contents of file
    print(file_contents.rstrip('\n'))

    # Extract numbers from file, calculate avg
    num_list = re.findall(r"[-+]?\d*\.\d+|\d+", file_contents)
    grades = [float(num) for num in num_list]
    average = mean(grades)

    # Print avg
    print('Average Grade:', format(average, '.2f'))

    # Close file
    grades_file.close()


def main():
    file_info()

    # Open file to append
    grades_file = open('grades.txt', 'a')

    while True:
        fwd = str(input('Add another student (Y/N): '))

        if fwd.lower() == 'y':
            while True:
                name = str(input("Enter student's name: "))

                if name.isdigit():
                    print("Please enter a valid name.")
                    continue
                else:
                    break

            while True:
                try:
                    grade = float(input("Enter student's grade: "))
                    if grade < 0:
                        print('Enter a number between 0-100.')
                        continue
                    elif grade > 100:
                        print('Enter a number between 0-100.')
                        continue
                    else:
                        grades_file.write(name + ' ' + str(grade) + '\n')
                        break
                except ValueError:
                    print('Enter a number between 0-100.')
                    continue

        elif fwd.lower() == 'n':
            grades_file.close()
            file_info()
            break

        else:
            print('Choose "Y" or "N"')


main()
