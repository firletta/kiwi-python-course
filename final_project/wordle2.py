import random
import os.path

try:
    file = open("words.txt","r")
except IOError:
    print("Error:\nFile with a list of words was not found. Make sure 'words.txt' is in the current directory.")
    exit()

words_file = open("words.txt","r") # source: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
words_data = words_file.read()
words_list = words_data.split()
word_to_guess = random.choice(words_list)
number_of_rounds = 6

def guess_the_word():
    user_input = input("Your guess: ")
    user_guess = user_input.lower()
    return user_guess

def error_message(error_type):
    if error_type == "incorrect_length":
        print(f"Invalid input. It has to be a {len(word_to_guess)}-letter word. Try again.")
    elif error_type == "word_not_found":
        print(f"Invalid input. The word was not found on the word list. Try again.")

def game_over_message():
    print(f"Game over. The Wordle is {word_to_guess.upper()}.")

class Styles:
    def green_tile(text):
        return f"\x1B[38;5;232m\x1B[48;5;42m[{text.upper()}]\033[0m"

    def yellow_tile(text):
        return f"\x1B[38;5;232m\x1B[48;5;214m[{text.upper()}]\033[0m"

    def grey_tile(text):
        return f"\x1B[38;5;232m\x1B[48;5;246m[{text.upper()}]\033[0m"

    def white_tile(text):
        return f"\x1B[38;5;232m\x1B[48;5;15m[{text.upper()}]\033[0m"


# printing game rules
print(f"\nWelcome to\n{Styles.green_tile('W')} {Styles.green_tile('O')} {Styles.green_tile('R')} {Styles.green_tile('D')} {Styles.green_tile('L')} {Styles.green_tile('E')}\n\n")
print(f"How To Play:\nGuess the word in {number_of_rounds} tries.\n- Each guess must be a  {len(word_to_guess)}-letter word.\n- The color of the tiles will change to show how close your guess was to the word.\n- You can quit game at any time by typing 'quit game'.\n\nExamples:")
print(f"\n{Styles.green_tile('w')} {Styles.white_tile('e')} {Styles.white_tile('a')} {Styles.white_tile('r')} {Styles.white_tile('y')}\n'W' is in the word and in the correct spot.")
print(f"\n{Styles.white_tile('p')} {Styles.yellow_tile('i')} {Styles.white_tile('l')} {Styles.white_tile('l')} {Styles.white_tile('s')}\n'I' is in the word but in the wrong spot.")
print(f"\n{Styles.white_tile('v')} {Styles.white_tile('a')} {Styles.white_tile('g')} {Styles.grey_tile('u')} {Styles.white_tile('e')}\n'U' is not in the word in any spot.\n")

# game below
for round in range(1,number_of_rounds+1):
    user_guess = guess_the_word()

    while user_guess not in words_list and user_guess != "quit game":
        if len(user_guess) != len(word_to_guess):
            error_message("incorrect_length")
        else:
            error_message("word_not_found")
        user_guess = guess_the_word()

    if user_guess == "quit game":
        game_over_message()
        break

    # creating list of correct letters
    green_tiles = []

    for i in range(len(word_to_guess)):
            if user_guess[i] == word_to_guess[i]:
                green_tiles.append(user_guess[i])

    # coloring users guess
    colored_user_guess = []

    for i in range(len(word_to_guess)):
        if user_guess[i] == word_to_guess[i]:
            colored_user_guess.append(Styles.green_tile(user_guess[i]))
        elif user_guess[i] in word_to_guess and green_tiles.count(user_guess[i]) + colored_user_guess.count(Styles.yellow_tile(user_guess[i])) < word_to_guess.count(user_guess[i]):
            colored_user_guess.append(Styles.yellow_tile(user_guess[i]))
        else:
            colored_user_guess.append(Styles.grey_tile(user_guess[i]))

    print(f"\n{round}. {' '.join(colored_user_guess)}\n")

    if round == number_of_rounds:
        game_over_message()

    if len(green_tiles) == len(word_to_guess):
        print(f"Congrats! You guessed the Wordle.")
        break