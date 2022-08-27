# importing colors module
from colors import *
# importing random module
from random import randint


def user_guess(guess_range):
    # generate random number base on the guess range
    generated_number = randint(1, guess_range)
    # User Guessing Attempt
    user_chance = 3
    for chance in range(3):
        user_guess = int(input(WHITE + "Provide Your Guess Number : "))
        # Determine / Validate User Guess
        if user_guess == generated_number:
            print(GREEN, f"Congratulation!!! You Guess {generated_number} ")
            break
        elif user_guess > generated_number:
            print(YELLOW, f" {user_guess} Too High, Try Again!!!")
            user_chance -= 1
        elif user_guess < generated_number:
            print(YELLOW, f"Too Low, {user_guess} Try Again!!!")
            user_chance -= 1

            if user_chance < 1:
                print(RED, f"You Failed, Try Again!!!!!\n"
                           f"The Correct Guess Number is {generated_number}")


# welcome  to Screen
def game_level():
    user_input = int(input(WHITE + "Choose Game Level\n "
                                   "1. Lazy (1 - 100)\n"
                                   "2. Intermediate (1 - 500)\n"
                                   "3. Hard (1 -  1000)\n"
                                   "provide Level: "))
    return user_input


def user_guess_range(user_input):
    guess_range = 0
    if user_input == 1:
        guess_range = 100
    elif user_input == 2:
        guess_range = 500
    elif user_input == 3:
        guess_range = 1000
    return guess_range


def welcome_screen():
    print(YELLOW, "***** welcome to Lover_Game ******")
    user_input = int(input(WHITE + " 1. Start Game\n "
                                   " 2. About Lover_ Game \n"
                                   " 3. Exit Application\n\n "
                                   "Choose An Option Above : "))

    # determine user input
    if user_input == 1:
        user_input = game_level()

        # Determine the guess range
        guess_range = user_guess_range(user_input)

        user_guess(guess_range)
    elif user_input == 2:
        print(YELLOW, "Loving Guessing Numbers")
    elif user_input == 3:
        print(WHITE, " Hope To see You Again Gamer. ")
        exit(1)
    else:
        print(RED, "Invalid Option, Try Again!!!!")


welcome_screen()
