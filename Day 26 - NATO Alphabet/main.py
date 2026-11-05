import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
nato_alphabet = {row.letter: row.code for (index, row) in data.iterrows()}

word = input("Enter a word: ").upper()
result = [nato_alphabet[letter] for letter in word if letter in nato_alphabet]
print(result)