# Write a program, that will take list of people:
# ["Michael", "Emilia", "John", "Peter", "Catherine", "Olivia", "Amy", "Oliver", "Thomas"]
# and filter out only people whose name starts with Vowel

names = ["Michael", "Emilia", "John", "Peter", "Catherine", "Olivia", "Amy", "Oliver", "Thomas"]
for i in range(len(names)):
    if names[i][0] in ["A", "E", "I", "O", "U"]:
        print(names[i])
