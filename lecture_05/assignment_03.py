people = []

while True:
    name = input("Enter name: ")
    surname = input("Enter surname: ")
    age = input("Enter age: ")

    person = {
	"name": name,
	"surname": surname,
    "age": age,
}

    people.append(person)

    choice = input("Do you want to continue? [y/n]")
    if choice == "n":
    	break

for person in people:
    for aspect, value in person.items():
        print(aspect + " is " + value)
    print("---")