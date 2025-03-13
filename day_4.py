#ROCK PAPER SCISSORS Game

rock_art = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''
paper_art = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''
scissors_art = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

import random

choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. "))
print("\nYour choice:")

if choice == 0:
    print(rock_art)
elif choice == 1:
    print(paper_art)
else:
    print(scissors_art)
    
print("\nComputer chose:")
comp_choice = random.randint(0, 2)
if comp_choice == 0:
    print(rock_art)
elif comp_choice == 1:
    print(paper_art)
else:
    print(scissors_art)

print("\n")
if choice == comp_choice:
    print("It's a draw")
else:
    if choice == 0:
        if comp_choice == 1:
            print("You lose")
        else:
            print("You win!")
    elif choice == 1:
        if comp_choice == 0:
            print("You win!")
        else:
            print("You lose")
    else:
        if comp_choice == 0:
            print("You lose")
        else:
            print("You win!")