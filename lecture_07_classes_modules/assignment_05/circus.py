# [x] Finish task
# [ ] Save files to drive

# [BONUS] Create the module circus.py with two classes:
# - Elephant – attributes name, weight and the method is_too_heavy that will return True if the
# elephant is heavier than 8 tons.
# - Lion – attributes name, age, methods is_too_old that will return True if the lion is older than 5 years.
# Module will contain two functions:
# - create_random_circus() – creates a list of one random lion (random name and age) and one random elephant (random name and weight).
# - filter_animals(animals) – filters animals that are too heavy (in case of the elephants) and too old (in case of the lions).
# Import this module to main.py, where you create and print random circus, then filter animals and print animals that are left.

import random

class Elephant:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
    def is_too_heavy(self):
        if self.weight > 8:
            return True
        else:
            return False

class Lion:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def is_too_old(self):
        if self.age > 5:
            return True
        else:
            return False


def create_random_circus():
    names = ["John","Andy","Joe","William","Emma","Olivia","Noah","Isabella","Mia","Sophia","Amelia","Jacob"]
    animals = {
        "elephant" : {
            "name" : random.choice(names),
            "weight" : random.randint(1,10)
        },
        "lion" : {
            "name" : random.choice(names),
            "age" : random.randint(1,16)
        }
    }
    return animals

def filter_animals(animals):
    if "elephant" in animals.keys():
        if "weight" in animals["elephant"].keys():
            circus_elephant = Elephant(animals["elephant"]["name"],animals["elephant"]["weight"])
        if circus_elephant.is_too_heavy() == True:
            animals.pop("elephant", None)
    if "lion" in animals.keys():
        if "age" in animals["lion"].keys():
            circus_lion = Lion(animals["lion"]["name"],animals["lion"]["age"])
        if circus_lion.is_too_old() == True:
            animals.pop("lion", None)
    return animals