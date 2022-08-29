dictionary = {}

while True:
    index = 0
    term = {}
    new_term = input("Enter a new term: ")
    term[new_term] = {}
    while True:
        index += 1
        new_definition = input("Definition: ")
        new_term[index] = new_definition
        term.update(new_term)
        choice = input(f"Do you want to add another definition of '{new_term}'? [y/n] ")
        if choice == "n":
            break
    choice = input("Do you want to add another term? [y/n] ")
    if choice == "n":
        dictionary.update(term)
        break
print(dictionary)

