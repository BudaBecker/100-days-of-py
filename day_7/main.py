import palavras
import arte
import random

print(arte.logo)
print(arte.vidas[-1])
word_to_guess = random.choice(palavras.words)
underline = '-' * len(word_to_guess)
lives = len(arte.vidas)-1
alredy_guessed = []

game_over = False
while not game_over:
    print(f"Word to guess: {underline}")
    guess_letter = input("Guess a letter: ")
    if guess_letter in alredy_guessed:
        print(f"You've already guessed {guess_letter}")
        print(arte.vidas[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    elif guess_letter in word_to_guess:
        new_underline = ''
        for i, letters in enumerate(word_to_guess):
            if letters == guess_letter:
                new_underline += letters
            else:
                new_underline += underline[i]
        underline = new_underline
        print(arte.vidas[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    else:
        lives -= 1
        print(f"You guessed '{guess_letter}', that's not in the word. You lose a life.")
        print(arte.vidas[lives])
        print(f"****************************{lives}/6 LIVES LEFT****************************")
    if underline == word_to_guess or guess_letter == word_to_guess:
        game_over = True
        print(f"It is {word_to_guess}!")
        print("You win.")
    if lives == 0:
        game_over = True
        print(f"***********************IT WAS {word_to_guess}! YOU LOSE**********************")
    alredy_guessed.append(guess_letter)