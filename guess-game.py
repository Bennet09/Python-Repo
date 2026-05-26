# Import the random module so we can generate random numbers
import random

# Generate a random number between 0 and 10
random_number = random.randint(0, 10)

# Ask the user to enter a guess
guess = int(input("Guess a number between 0 and 10: "))

# Check if the user's guess is correct
if guess == random_number:
    print("Congratulations! You guessed correctly.")
else:
    # Display the correct number if the guess is wrong
    print("Sorry, that is incorrect.")
    print("The correct number was:", random_number)