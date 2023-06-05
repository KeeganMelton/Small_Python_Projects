import random

# lists of numbers, letters, and symbols
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
           'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
symbols = ["!", "@", "#", "$", "%", "^", "&", "*"]

# asks user for password length and number of numbers, symbols, and letters to use
password_size = int(input("How long do you want your password to be? \n"))
numbers_to_use = int(input("How many numbers do you want to use? \n"))
symbols_to_use = int(input("How many symbols do you want to use? \n"))
letters_to_use = int(input("How many letters do you want to use? \n"))

# holds the new password
new_password = []

# gathers random letters
for i in range(0, letters_to_use):
    random_letter = random.randint(0, 25)
    new_password.append(letters[random_letter])

# gathers random numbers
for i in range(0, numbers_to_use):
    random_num = random.randint(0, 9)
    new_password.append(numbers[random_num])

# gathers random symbols
for i in range(0, symbols_to_use):
    random_sym = random.randint(0, 7)
    new_password.append(symbols[random_sym])

# empty string to add characters
password = ""

# adds selected characters to the 'password' string
random.shuffle(new_password)
for i in range(0, password_size):
    password = password + new_password[i]

# displays new password
print(password)
