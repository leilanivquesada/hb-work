"""A number-guessing game."""
import random

# Put your code here
# greet player
print("Hi there! What's your name?")
#get player name
name = input("Input your name here ")
print(name + ", let's play a guessing game!")
print(f"{name}, I'm thinking of a number between 1 and 100.")
print("Try to guess my number.")
# choose a random number between 1 and 100
secret_number = random.randint(1, 100)
#repeat forever:

pick = int(input("Your guess? "))
counter = 1
while pick != secret_number:
    if pick > secret_number:
        print("Your guess is too high, try again.")
    else:
        print("Your guess is too low, try again.")
    pick = int(input("Your guess? "))
    counter += 1 
print(f"Well done, {name}! You found my number in {counter} tries!")

