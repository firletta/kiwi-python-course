"""
TODO
Add a feature to the dictionary application that allows users to store new definitions. This means that when
the application is run, it should ask user whether they want to `search`, `add` a definition or just `exit`.
If they want to search for a term, the application lets them search just as before. If they want to add a definition,
the application asks them for a term and then keeps asking them for the definitions until they say that they don't
want to add more definitions. The application then saves the term with its definitions so it can be searched for.
After `add` or `search` operations finish, the application should again ask the user if they want to search, add or
exit. Selecting `exit` terminates the program (you can add a goodbye message). Optionally, if you feel on a roll
when you have this functionality, you can add `delete` action as well for deleting terms.
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

users_action = input("What would you like to do?\nType:\n- 'search' to look up definition of a term\n-'add' to add new definition\n- 'exit' to exit the dictionary  ")

if users_action == "search": #searching
    look_up = input("Enter a word: ")
    if look_up in dictionary.keys():
        print("Definition of '" + look_up + "':")
        for index_number, definition in dictionary[look_up].items():
            print(index_number + " - " + definition)
    else:
        print("Definition was not found.")
elif user_action == "add":


        choice = input("Do you want to continue? [y/n]")
        if choice == "n":
            break