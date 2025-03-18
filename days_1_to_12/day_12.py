art = '''
   ___                       _____ _                __                __
  / _ \_   _  ___  ___ ___  /__   \ |__   ___    /\ \ \_   _ _ __ ___ | |__   ___ _ __ 
 / /_\/ | | |/ _ \/ __/ __|   / /\/ '_ \ / _ \  /  \/ / | | | '_ ' _ \| '_ \ / _ \ '__|
/ /_\\\| |_| |  __/\__ \__ \  / /  | | | |  __/ / /\  /| |_| | | | | | | |_) |  __/ |   
\____/ \__,_|\___||___/___/  \/   |_| |_|\___| \_\ \/  \__,_|_| |_| |_|_.__/ \___|_|
'''

from random import randint

print(art)
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
number = randint(1, 100)
if difficulty == "easy":
    lives = 10
else:
    lives = 5

while True:
    print(f"You have {lives} attempts remaining to guess the number.")
    guess = int(input("Make a Guess: "))
    if guess == number:
        print(f"You got it! The answer was {number}.")
        break
    elif guess > number:
        print("Too high.")
        lives -= 1
    else:
        print("Too low.")
        lives -= 1
    if lives <= 0 :
        print(f"You've run out of guesses. The answer was {number}")
        break
    print("Guess Again.")