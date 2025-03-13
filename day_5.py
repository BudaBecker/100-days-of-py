letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
           'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

import random

print("Welcome to the PyPassword Generator!")
number_letters = int(input("How many letters would you like in your password?\n"))
number_numbers = int(input("How many numbers?\n"))
number_symbols = int(input("How many symbols?\n"))

password = []
for i in range(number_letters):
    password.append(random.choice(letters))
for i in range(number_numbers):
    password.append(random.choice(numbers))
for i in range(number_symbols):
    password.append(random.choice(symbols))
                    
print(password)
random.shuffle(password)
print(password)

word_password = ""
for chars in password:
    word_password += chars
print(f"Your new password is: {word_password}")