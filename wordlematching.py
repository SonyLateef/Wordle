def clue(word, guess):
    wordle_clue = ""
    for i in range(len(word)):
        if word[i] == guess[i]:
            wordle_clue += word[i].upper()
        elif guess[i] in word:
            wordle_clue += guess[i].lower()
        else:
            wordle_clue += "-"
    print(wordle_clue)

clue("stair", "steer")