# A simple guessing game.
# The computer randomly picks a number between 1 & 100.
# Uses repeatedly guesses until correct # is found.

from random import randrange

def game1():
    print("I will think of a random number between 1 & 100.")
    print ("Can you guess the correct number? ")

    correct = randrange(1,101)
    guess = int(input("What is your first guess? "))
    while guess != correct:
        # Give the user feedback, letting them know whether
        # the guess was too high or too low.
        if guess > correct:
            print("Your guess is too high.")
        else:
            print("Your guess is too low.")
        
        guess = int(input("Sorry, try again: " ))

    print("Yay! You found the number!")
    return

if __name__ == "__main__":
    game1()