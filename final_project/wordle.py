import random


class Styles:
    def green_tile(text):
        return f"\033[1;42m[{text.upper()}]\033[0m "

    def yellow_tile(text):
        return f"\033[1;43m[{text.upper()}]\033[0m "

    def white_tile(text):
        return f"\033[1;47m[{text.upper()}]\033[0m "

    def black_tile(text):
        return f"\033[1m[{text.upper()}]\033[0m "


words_file = open("words.txt","r")
words_data = words_file.read()
words_list = words_data.split()
word_to_guess = random.choice(words_list)


# printing rules
print(f"\nWelcome to\n{Styles.green_tile('W')}{Styles.green_tile('O')}{Styles.green_tile('R')}{Styles.green_tile('D')}{Styles.green_tile('L')}{Styles.green_tile('E')}\n\n")
print(f"How To Play:\nGuess the word in 6 tries.\n- Each guess must be a 5-letter word.\n- The color of the tiles will change to show how close your guess was to the word.\n\nExamples:")
print(f"\n{Styles.green_tile('w')}{Styles.black_tile('e')}{Styles.black_tile('a')}{Styles.black_tile('r')}{Styles.black_tile('y')}\n'W' is in the word and in the correct spot.")
print(f"\n{Styles.black_tile('p')}{Styles.yellow_tile('i')}{Styles.black_tile('l')}{Styles.black_tile('l')}{Styles.black_tile('s')}\n'I' is in the word but in the wrong spot.")
print(f"\n{Styles.black_tile('v')}{Styles.black_tile('a')}{Styles.black_tile('g')}{Styles.white_tile('u')}{Styles.black_tile('e')}\n'U' is not in the word in any spot.\n")