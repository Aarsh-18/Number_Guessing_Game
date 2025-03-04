from random import *
from math import *

lower=int(input("Enter Lower Bound: ")) # lower boundary of the range of number
upper=int(input("Enter Upper Bound: ")) # upper boundary of the range of number

num=randint(lower,upper) # generate random number based on the lower and upper boundaries
max_guess=int(log2(upper-lower+1))+1 # initialize the maximum guesses user gets

count=0 # initialize count variable to 0
while count<max_guess: # while loop to iterate until user wins or looses
    guessed_correctly=False # flag initially set to false
    guess=int(input("Guess a number: ")) # user input to guess a number
    count+=1 # increment count by 1
    if guess==num: # if user correctly guesses the number
        print("Congratulations! You guessed in ",count,"attempts.") # prints that user won and no. of attempts used by him/her
        guessed_correctly=True # flag set to true if user wins
        break # break the loop if user wins

    elif guess<num: # if the user guess is less than the number.
        print("Incorrect guess! You guessed too small!")
        print("You have",max_guess-count,"attempts left.")

    elif guess>num: # if the user guess is greater than the number.
        print("Incorrect guess! You guessed too high!")
        print("You have",max_guess-count,"attempts left.")

if not guessed_correctly: # if the user looses
    print("The number is ",num)
    print("Better luck next time.")
