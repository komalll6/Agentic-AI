import random
print("Welcome to the Magic Numbers Game!")
print("I have selected a random number between 1 and 100.")
number = random.randint(1, 100)
guess = -1
while guess != number:
    guess = int(input("Please enter your guess:"))
    if guess == number:
        print("Congratulations! You guessed the correct number:", number)
    elif guess > number:
        print("Your number is too high. Try again.")
    else:
        print("Your number is too low. Try again.")