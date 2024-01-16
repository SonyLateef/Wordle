import random

def clue(word, guess):
    wordle_clue = ""
    for i in range(len(word)):
        if word[i] == guess[i]:
            wordle_clue += word[i].upper()
        elif guess[i] in word:
            wordle_clue += guess[i].lower()
        else:
            wordle_clue += "-"
    return wordle_clue

with open("words.txt", "r") as wordfile:
    words = [word.strip() for word in wordfile.readlines() if len(word.strip()) == 5]

def game():
    wordle_word = random.choice(words)
    guesses = 0
    while guesses < 6:
        guess = input("Guess a word: ")
        guesses += 1
        if len(guess) > 5:
            print("The word must be less than 5 letters.")
            continue
        if guess == wordle_word:
            print("You guessed the word")
            return
        else:
            wordle_clue = clue(wordle_word, guess)
            print(wordle_clue)
    print("You ran out of guesses, the word was: ", wordle_word)
    play_again()

def play_again():
    while True:
        play_again = input("Do you want to play again? (yes or no) ")
        if play_again == "yes":
            game()
        else:
            break

game()
