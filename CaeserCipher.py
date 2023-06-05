# list of letter in the alphabet
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
again = True

# encrypts the user's message by the about entered by the user
def encrypt(message, shift):
    encrypted_word = ''
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            encrypted_word += alphabet[(position + shift) % 26]
    print(encrypted_word + "\n")

# decrypts the user's message by the about entered by the user
def decrypt(message, shift):
    decrypted_word = ''
    for char in message:
        if char in alphabet:
            position = alphabet.index(char)
            decrypted_word += alphabet[(position - shift) % 26]
    print(decrypted_word + "\n")

# user selection to "encrypt" or "decrypt" a message
while again == True:
    user_choice = input("Do you want to 'encrypt' or 'decrypt' a message? \n").lower()

    # asked user to enter a message to encrypt and how many letters to shift the message
    if user_choice == 'encrypt':
        message = input("Enter a message you would like to encrypt: \n")
        shift = int(input("How many letters do you want to shift the message by? \n"))
        encrypt(message, shift)

    # asked user to enter a message to decrypt and how many letters to shift the message
    if user_choice == 'decrypt':
        message = input("Enter a message you would like to decrypt: \n")
        shift = int(input("How many letters do you want to shift the message by? \n"))
        decrypt(message, shift)

    # loops if "encrypt" or "decrypt" are not entered
    else:
        print("Please enter a valid input\n")

    go_again = input("Do you want to encrypt or decrypt another word? (y\\n)? \n")
    if go_again == 'y':
        again = True
    else:
        again = False