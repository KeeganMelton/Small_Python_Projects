import random

# random word bank
word_list = ["apple", "banana", "carrot"]

# selects a random word
randNum = random.randint(0, len(word_list) - 1)
selected_word = word_list[randNum]

# lists for showing the selected word and letters guessed
show_word = []
guessed_letter = []

wrong_guess_count = 0

# shows "_" for letters not yet guessed
for n in selected_word:
    show_word.append("_")

# reveals correctly guessed letters
while show_word.__contains__("_"):
    match = False
    print(f"{show_word}")
    letter_guess = input("Guess a letter: ").lower()

    if guessed_letter.__contains__(letter_guess):
        print("You have already guessed that letter")

    for position in range(len(selected_word)):
        if selected_word[position] == letter_guess:
            show_word[position] = letter_guess
            match = True

    if not match:
        wrong_guess_count += 1
        print(f"You have {5 - wrong_guess_count} guess(es) remaining")

    guessed_letter.append(letter_guess)

    if wrong_guess_count == 5:
        break


if show_word.__contains__("_"):
    print("You Lose!")
    print(f"The word is {selected_word}")
    print("Better luck next time.")
else:
    print("You Win!!")
    print(f"The word is {selected_word}")