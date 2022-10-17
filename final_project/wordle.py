import random


class Styles:
    def green_tile(text):
        return f"\x1B[38;5;232m\x1B[48;5;42m[{text.upper()}]\033[0m"

    def yellow_tile(text):
        return f"\x1B[38;5;232m\x1B[48;5;214m[{text.upper()}]\033[0m"

    def grey_tile(text):
        return f"\x1B[38;5;232m\x1B[48;5;246m[{text.upper()}]\033[0m"

    def white_tile(text):
        return f"\x1B[38;5;232m\x1B[48;5;15m[{text.upper()}]\033[0m"


words_file = open("words.txt","r") # source: https://www-cs-faculty.stanford.edu/~knuth/sgb-words.txt
words_data = words_file.read()
words_list = words_data.split()
word_to_guess = random.choice(words_list)


# printing game rules
print(f"\nWelcome to\n{Styles.green_tile('W')} {Styles.green_tile('O')} {Styles.green_tile('R')} {Styles.green_tile('D')} {Styles.green_tile('L')} {Styles.green_tile('E')}\n\n")
print(f"How To Play:\nGuess the word in 6 tries.\n- Each guess must be a 5-letter word.\n- The color of the tiles will change to show how close your guess was to the word.\n\nExamples:")
print(f"\n{Styles.green_tile('w')} {Styles.white_tile('e')} {Styles.white_tile('a')} {Styles.white_tile('r')} {Styles.white_tile('y')}\n'W' is in the word and in the correct spot.")
print(f"\n{Styles.white_tile('p')} {Styles.yellow_tile('i')} {Styles.white_tile('l')} {Styles.white_tile('l')} {Styles.white_tile('s')}\n'I' is in the word but in the wrong spot.")
print(f"\n{Styles.white_tile('v')} {Styles.white_tile('a')} {Styles.white_tile('g')} {Styles.grey_tile('u')} {Styles.white_tile('e')}\n'U' is not in the word in any spot.\n")


for round in range(1,7):
    user_input = input("Your guess: ")
    user_guess = user_input.lower()

    while len(user_guess) != 5:
        user_input = input("Invalid input. It has to be a valid 5-letter word. Try again: ")
        user_guess = user_input.lower()

    while user_guess not in words_list:
        user_input = input("Invalid input. It has to be a valid 5-letter word. Try again: ")
        user_guess = user_input.lower()

    colored_user_guess = []
    green_tiles_count = 0

    for i in range(len(word_to_guess)):
        if user_guess[i] == word_to_guess[i]:
            colored_user_guess.append(Styles.green_tile(user_guess[i]))
            green_tiles_count += 1
        elif user_guess[i] in word_to_guess:
            colored_user_guess.append(Styles.yellow_tile(user_guess[i]))
        else:
            colored_user_guess.append(Styles.grey_tile(user_guess[i]))

    print(f"\n{round}. {' '.join(colored_user_guess)}\n")

    if round == 6:
        print(f"Game over. The Wordle is {word_to_guess.upper()}.")

    if green_tiles_count == 5:
        print(f"Congrats! You guessed the Wordle.")
        break