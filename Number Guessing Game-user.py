from random import *
from math import *

lower = int(input("Enter Lower Bound: "))  # lower boundary of the range of number
upper = int(input("Enter Upper Bound: "))  # upper boundary of the range of number

max_guess = int(log2(upper - lower + 1)) + 1  # initialize the maximum guesses user gets
feedback = '' # initial user feedback is empty string
count = 0  # initialize count variable to 0
print("The computer has ", max_guess, "attempts to guess the number correctly.")
# informs the user about the number of guesses remaining

while count < max_guess:  # while loop to iterate until user wins or looses
    guessed_correctly = False   # flag initially set to false
    guess = randint(lower, upper) # computer guess random number as per the boundaries
    feedback = input(f"Is {guess} too high(H), too low(L), or correct(C)? ").lower()
    # user gives feedback to the computer according to the computer's guess
    count += 1  # increment count by 1
    if feedback == 'c': # if computer guessed the number correctly
        print("The computer guessed the number", str(guess), "correctly in", count, "attempts!")
        guessed_correctly = True # flag set to true
        break # break the while loop here

    elif feedback == 'l': # if computer guessed smaller number
        lower = guess + 1 # set lower boundary to guess+1
        print("The computer got", max_guess - count, "attempts left.")

    elif feedback == 'h': # if computer guessed larger number
        upper = guess - 1 # set upper boundary to guess-1
        print("The computer got", max_guess - count, "attempts left.")

if not guessed_correctly: # if computer looses
    print("The computer failed to guess the number correctly in the provided", count,"attempts!")
