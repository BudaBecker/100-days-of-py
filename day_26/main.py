import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")

alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

name = input("Type your name: ").upper()

nato_name = [alphabet[letters] for letters in name if letters in alphabet.keys()]

print(nato_name)