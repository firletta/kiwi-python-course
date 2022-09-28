# Create an application with the class Dog and attributes name and age.
# Add a method bark that will print the name of the dog and the “barks” word – <NAME_OF_DOG> barks!
# Create two dogs with the different names and call the bark method on both of them.

class Dog:
    def __init__(self, name):
        self.name = name
    def bark(self):
        print(self.name, "barks!")

dog1 = Dog("Snoopy")
dog2 = Dog("Pati")

dog1.bark()
dog2.bark()