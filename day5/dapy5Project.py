import random
import string

letters = list(string.ascii_lowercase)
numbers = [i for i in range(1, 10)]
symbols = ["@", "#", "$", "%", "^", "&", "*", "!", "?", "+", "="]

number_of_letters = int(input("number of letters in the password: "))

number_of_numbers = int(input("number of numbers in the password: "))

number_of_symbols = int(input("number of symbols in the password: "))

letter_combination = ""
numbers_combinations = ""
symbols_combinations = ""
password_combination = []
password = ""

for i in range(number_of_letters):
    letter = random.choice(letters)
    letter_combination += letter

for i in range(number_of_numbers):
    number = random.choice(numbers)
    numbers_combinations += str(number)

for i in range(number_of_symbols):
    symbol = random.choice(symbols)
    symbols_combinations += symbol

password_combination = [letter_combination, numbers_combinations, symbols_combinations]
for i in range(len(password_combination)):
    rand_indx = random.randint(0, 3)
    password_combination[i], password_combination[rand_indx] = (
        password_combination[rand_indx],
        password_combination[i],
    )

for i in password_combination:
    password += i

print(password)
