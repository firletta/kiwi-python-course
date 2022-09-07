"""
Create a real dictionary application. Each term stored in the dictionary can have multiple definitions. Pre-load it with
some data and let the user search for the terms in it by inputting the searched term. When the searched term is missing,
return an error message to the user explaining what's wrong. Otherwise print the term and its definitions in the
following structure. See an example for the term `deadline`

Definition of deadline:
1 - a line drawn within or around a prison that a prisoner passes at the risk of being shot
2 - a date or time before which something must be done
"""

dictionary = {
    "cat": {
        "1": "noun - a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed.",
        "2": "noun - (especially among jazz enthusiasts) a man.",
        "3": "verb - raise (an anchor) from the surface of the water to the cathead."},
    "dog": {
        "1": "noun - a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice.",
        "2": "verb - follow (someone) closely and persistently.",
        "3": "verb - act lazily; fail to try one's hardest."},
    "rabbit": {
        "1": "noun - a gregarious burrowing plant-eating mammal, with long ears, long hind legs, and a short tail.",
        "2": "noun - a conversation.",
        "3": "verb - hunt rabbits.",
        "4": "verb - talk at length, especially about trivial matters."}
    }

look_up = input("Enter a word: ")
if look_up in dictionary.keys():
    print("Definition of '" + look_up + "':")
    for index_number, definition in dictionary[look_up].items():
        print(index_number + " - " + definition)
else:
    print("Definition was not found.")
