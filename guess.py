#!/usr/bin/python3

secret_number = 8

while True:
    guess = int(input("Enter your number: "))

    if (guess == secret_number):
        print("you have guessed it")
        break

