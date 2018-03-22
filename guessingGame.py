# This is a guess the numbers game

import random

print('Hello. What is your name?')
name = input()
secretNumber = random.randint(1, 100)
print('Well, '+ name +', I am thinking of a number bewteen 1 and 100')

# Ask the player to guess 10 times
for guessesTaken in range(1, 10):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is to low')
    elif guess > secretNumber:
        print('Your guesss is to high')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good Job, '+ name + '! You guessed the right number in '+ str(guessesTaken) +' guesses')
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber))
