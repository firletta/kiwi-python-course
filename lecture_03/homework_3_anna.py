# Print all three letter words in alphabetical order.
# We consider only small english letter a-z, the words don't need to be valid english words.
# There are 17576 unique words to print (e.g. axy, bnm, can, tlk, ...)
# You can use helper function chr, that will translate number to letter (in order of ASCII)
# chr(97) == "a", chr(98) == "b", ..., chr(122) == "z"

for a in range(97,123):
    for b in range(97,123):
        for c in range(97,123):
            print(chr(a)+chr(b)+chr(c))