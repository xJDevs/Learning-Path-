
import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
user_letters = int(input("How many letters would you like in your password?\n"))
user_symbols = int(input(f"How many symbols would you like?\n"))
user_numbers = int(input(f"How many numbers would you like?\n"))

# easy version = all characters added in sequence as entered by user
password = ''
for _ in range(user_letters):
    password += random.choice(letters)

for _ in range(user_symbols):
    password += random.choice(symbols)

for _ in range(user_numbers):
    password += random.choice(numbers)


print(f'Easy version: {password}\n')

# hard version = all characters shuffled

pass_str_to_list = list(password) # converts it to list so shuffle below can read it
random.shuffle(pass_str_to_list)
strong_password = ''.join(pass_str_to_list)
print(f'Hard version: {strong_password}')



