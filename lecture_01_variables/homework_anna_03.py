# ask user for 3 words and 1 random character. Then concatenate them using the last character with no other spaces
# e.g. for "Tom", "Martin", "Peter", and "-" prints "Tom-Martin-Peter"

word_a = input("Enter first word: ")
word_b = input("Enter second word: ")
word_c = input("Enter third word: ")
character = input("Enter a random character:")

print(word_a, word_b, word_c, sep=character)