def play_hangman(word):
    won = False
    wrong = 0
    letters = list(word)
    guessed_letters = []
    board = ["_"] * len(word)
    stages = [
              "________ ",
              "|  | ",
              "|  0 ",
              "| /|\ ",
              "| / \ "
              ]

    def show_progress():
        print("\nWord: {0}".format(" ".join(board)))
        print("\nPrevious Guesses: {0}".format(" ".join(guessed_letters)))
        print("\n".join(stages[0:wrong+1]))

    show_progress()
    while wrong < len(stages) - 1 and not won:
        msg = "\nChoose the next letter: "
        chosen_letter = input(msg)
        guessed_letters.append(chosen_letter)
        if chosen_letter in letters:
            char_idx = letters.index(chosen_letter)
            board[char_idx] = chosen_letter
            letters[char_idx] = "$"
        else:
            wrong = wrong + 1
        show_progress()
        if"_" not in board:
            won = True
    if won:
        print("\nYou win!")
    else:
        print("\nYou lose!")
        print("The word is: {0}".format(word))


if __name__ == "__main__":
    given_word = "python"
    play_hangman(given_word)
