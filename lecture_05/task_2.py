"""
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
    "cat": ["noun - a small domesticated carnivorous mammal with soft fur, a short snout, and retractable claws. It is widely kept as a pet or for catching mice, and many breeds have been developed.","noun - (especially among jazz enthusiasts) a man.","verb - raise (an anchor) from the surface of the water to the cathead."],
    "dog": ["noun - a domesticated carnivorous mammal that typically has a long snout, an acute sense of smell, non-retractable claws, and a barking, howling, or whining voice.","verb - follow (someone) closely and persistently.","verb - act lazily; fail to try one's hardest."],
    "rabbit": ["noun - a gregarious burrowing plant-eating mammal, with long ears, long hind legs, and a short tail.","noun - a conversation.","verb - hunt rabbits.","verb - talk at length, especially about trivial matters."]
    }

while True:
    user_action = input("What would you like to do?\nType:\n- 'search' to look up definition of a term\n-'add' to add new definition\n- 'exit' to exit the dictionary\n")
    if user_action == "search": #searching
        look_up = input("Enter a word: ")
        if look_up in dictionary.keys():
            print("Definition of '" + look_up + "':")
            index_number = 0
            for i in range(len(dictionary[look_up])):
                print(str(index_number + 1) + " - " + dictionary[look_up][i])
                index_number += 1
        else:
            print("Definition was not found.")
    elif user_action == "add":
        while True:
            new_term = input("Enter a new term: ")
            dictionary[new_term] = []
            while True:
                new_definition = input("Definition: ")
                dictionary[new_term].append(new_definition)
                choice = input(f"Do you want to add another definition of '{new_term}'? [y/n] ")
                if choice == "n":
                    break
            choice = input("Do you want to add another term? [y/n] ")
            if choice == "n":
                break
            choice = input("Do you want to continue? [y/n]")
            if choice == "n":
                break
    else:
        print("Bye bye!")
        break