#!/usr/bin/env python3

# Created by: Teddy Sannan
# Created on: September 2019
# This lets the user guess a number

import random


def main():
    # random number
    number = random.randint(0, 9)

    # input
    guess = int(input("Guess my number between 0 and 9: "))

    # process
    if guess == number:
        # output
        print()
        print("Correct! My number was", number)

    # process
    if guess != number:
        # output
        print()
        print("Sorry. Better luck next time")
        print("My number was", number)


if __name__ == "__main__":
    main()
