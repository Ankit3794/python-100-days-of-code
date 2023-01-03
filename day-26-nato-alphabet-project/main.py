import pandas as pd

nato = pd.read_csv("nato_phonetic_alphabet.csv")

final_dict = {row.letter: row.code for index, row in nato.iterrows()}

# final_dict = dict(nato.values)
name = input("Enter your name: ")
nato_result = [final_dict.get(i.upper()) for i in name]
print(nato_result)
