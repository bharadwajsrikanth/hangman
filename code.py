from enum import Enum
import csv
import random

class Genres(Enum):
    Movies = 1
    Sports = 2


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

    def find_occurrences(list, ch):
        return [i for i, x in enumerate(list) if x == ch]

    show_progress()
    while wrong < len(stages) - 1 and not won:
        msg = "\nChoose a letter: "
        chosen_letter = input(msg)
        guessed_letters.append(chosen_letter)
        if chosen_letter in letters:
            indices = find_occurrences(letters, chosen_letter)
            for idx in indices:
                board[idx] = chosen_letter
                letters[idx] = "$"
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


def get_genre():
    print("\nAvailable Genres")
    for i in range(len(Genres)):
        print("{0}. {1}".format(i+1, Genres(i+1).name))
    msg = "\nChoose a genre: "
    return input(msg)


def get_word(genre):
    movies_filename = 'movies'
    sports_filename = 'sports'

    if genre == 1:
        filename = movies_filename + '.csv'
    elif genre == 2:
        filename = sports_filename + '.csv'

    with open(filename) as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        for lines in csv_reader:
            words = lines

    return random.choice(words)



if __name__ == "__main__":
    selected_genre = int(get_genre())
    print("\nSelecting a word from {0} genre".format(Genres(selected_genre).name))
    given_word = get_word(selected_genre)
    play_hangman(given_word)
