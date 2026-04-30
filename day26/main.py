import pandas as pd

phoenetic = pd.read_csv("./day26/nato_phonetic_alphabet.csv")
phonetic_dict = {rows.letter: rows.code for (index, rows) in phoenetic.iterrows()}

name = input("enter you name: ")

phonetic_list = [phonetic_dict[letter.upper()] for letter in name]

print(phonetic_list)
