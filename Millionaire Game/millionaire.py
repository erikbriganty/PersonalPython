# File name: millionaire.py
# Name: Erik Briganty
# Date: 04/26/20

import re


def question1():
    print('This first question will be worth 100 points.\n'
          + 'Are you ready?\n')

    print("1. Who was the winner of a People's Choice Award"
          + "for Animal Star in 2019?\n"
          + "A) Pablo the Pug\n"
          + "B) Doug the Pug\n"
          + "C) Rojo the LLama\n"
          + "D) Grumpy Cat")

    while True:
        verify = re.compile('^[a-dA-D]+$')

        ans = str(input("Answer: "))

        if ans.lower() == 'b':
            print("\nI can't believe you know that.\n"
                  + "You gained 100 points!")
            return 100
        elif not verify.match(ans):
            print("Choose from the list of answers.")
            continue
        else:
            print("Tough luck. That is incorrect.\n")
            return 0


def question2():
    print("Alright, moving on.\n"
          + "This next question is worth 200 points.\n"
          + "Make it count.\n")

    print('2. How many legitimate children does Michael Jackson have?\n'
          + 'A) Three\n'
          + 'B) One\n'
          + 'C) Seven\n'
          + 'D) Sixteen')

    while True:
        verify = re.compile('^[a-dA-D]+$')

        ans = str(input("Answer: "))

        if ans.lower() == 'a':
            print("\nYou have way too much time on your hands.\n"
                  + "You have gained 200 points!\n")
            return 200
        elif not verify.match(ans):
            print("Choose from the list of answers.")
            continue
        else:
            print("Ouch. You're not very good at this.\n")
            return 0


def question3():
    print("We're almost at the finish line.\n"
          + 'This question is worth 500 points.')

    print('3. In what year did Brittany Spears shave her head?\n'
          + 'A) 2003\n'
          + 'B) 1998\n'
          + 'C) 2007\n'
          + 'D) 2010')

    while True:
        verify = re.compile('^[a-dA-D]+$')

        ans = str(input("Answer: "))

        if ans.lower() == "c":
            print("\nShould we talk about why you know this?\n"
                  + "You have gained 500 points!\n")
            return 500
        elif not verify.match(ans):
            print("Choose from the list of answers.")
            continue
        else:
            print("Have you thought about just quitting?\n")
            return 0


def question4():
    print("I'm getting just as excited as you are.\n"
          + 'This one is worth a whopping 1,000 points\n')

    print("What is the capital of Somalia?\n"
          + 'A) Mogadishu\n'
          + 'B) Bujumbura\n'
          + 'C) Luanda\n'
          + 'D) Praia')

    while True:
        verify = re.compile('^[a-dA-D]+$')

        ans = str(input("Answer: "))

        if ans.lower() == "a":
            print("\nEven I had to google this one.\n"
                  + "You have gained 1,000 points!\n")
            return 1000
        elif not verify.match(ans):
            print("Choose from the list of answers.")
            continue
        else:
            print("Nobody blames you.\n")
            return 0


def question5():
    print("This is the last question.\n"
          + "It's worth 2,000 points.\n"
          + "Don't mess up.")

    print("Who is Kim Jong Un's wife?\n"
          + "A) Jennifer Lopez\n"
          + "B) Ri Sol-ju\n"
          + "C) Kim Jung-sook\n"
          + "D) Peng Liyuan")

    while True:
        verify = re.compile('^[a-dA-D]+$')

        ans = str(input("Answer: "))

        if ans.lower() == "b":
            print("\nEveryone knows this one!\n"
                  + "You have gained 2,000 points!\n")
            return 2000
        elif not verify.match(ans):
            print("Choose from the list of answers.")
            continue
        else:
            print("This is the easiest one!\n")
            return 0


def main():

    while True:
        name = str(input("Enter your name: "))

        if name.isdigit():
            print('Please enter a valid name.')
            continue
        else:
            break

    print("Welcome", name
          + " to the WalMart version of..\n"
          + "WHO WANTS TO BE A MILLIONAIRE!!\n")

    while True:
        total_points = 0

        # Question 1
        total_points += question1()
        print("Your total points are", total_points,
              '\n')

        # Question 2
        total_points += question2()
        print("Your total points are", total_points,
              '\n')

        # Question 3
        total_points += question3()
        print("Your total points are", total_points,
              '\n')

        # Question 4
        total_points += question4()
        print("Your total points are", total_points,
              '\n')

        # Question 5
        total_points += question5()
        print("Your total points are", total_points,
              '\n')

        import os
        txt_file = 'highscore.txt'
        score = total_points

        # if the text file doesn't exists write the current score as high score
        if not os.path.exists(txt_file):
            with open(txt_file, 'w') as f:
                f.write(f'Score: {score}\n'
                        + f'Name: {name}')
            print('Your score has been saved.')

        # read the score
        with open(txt_file, 'r') as f:
            previous_score = int(f.readline().split()[-1])

        # compare the previous score with current score and write the highest score
        if previous_score <= score:
            with open(txt_file, 'w') as f:
                f.write(f'Score: {score}\n'
                        + f'Name: {name}')
            print('Congratulations! You have the high score!')

        # Ask user to play again
        while True:
            play_again = str(input('Would you like to play again? (Y/N): '))

            if play_again.lower() == 'y':
                break
            elif play_again.lower() == 'n':
                exit()
            else:
                print('Please answer "Y" or "N".')


main()
