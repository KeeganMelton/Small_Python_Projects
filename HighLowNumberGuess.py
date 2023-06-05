import random

play_again = True

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")

# checks if the users guess is higher, lower, or equal to the number
def guess(attempts):
    user_guess = int(input("What is your guess?: "))
    if 100 < user_guess or user_guess < 0:
        print("Please guess a number in the range of 1 - 100")
        win = False
        return attempts, win

    if user_guess > randomNum:
        print("Too High\n")
        attempts -= 1
        win = False
        return attempts, win

    if user_guess < randomNum:
        print("Too Low\n")
        attempts -= 1
        win = False
        return attempts, win

    if user_guess == randomNum:
        print("You Guessed the Number!!\n")
        attempts -= 1
        win = True
        return attempts, win

while play_again == True:

    difficulty_selection_valid = False
    attempts = 0
    win = False

    # asks user to select a difficulty
    # sets number of attempts based on selection
    while difficulty_selection_valid == False:
        difficulty = input("Please select a difficulty buy typing 'easy' or 'hard': \n").lower()
        if difficulty == 'easy':
            attempts = 10
            difficulty_selection_valid = True
        elif difficulty == 'hard':
            attempts = 5
            difficulty_selection_valid = True
        else:
            difficulty_selection_valid = False
    randomNum = random.randint(1, 100)

    while attempts > 0:
        print(f"You have {attempts} to guess the correct number")
        attempts, win = guess(attempts)
        if win == True:
            break
    if input("Would you like to play again? (y\\n)").lower() == 'y':
        play_again = True
    else:
        play_again = False