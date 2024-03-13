# Program to guess the random number 

import random

range = input("Enter the number up to which you want to guess:\t")

if range.isdigit():
    range = int(range)

    if range <= 0:
        print("Enter the number greater than zero")
        quit()

else:
    print("Enter the number next time")
    quit()


random_num = random.randint(0,range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess within a range:\t")

    if user_guess.isdigit():
        user_guess = int(user_guess)

    else:
        print("Enter the number next time")
        continue

    if user_guess == random_num:
        print("You have succesflly guessed the number!!!")
        break

    else:
        print("**You have guessed the number incorrectly**")


print("\n You have guessed the answer in",guesses,"attempt")



