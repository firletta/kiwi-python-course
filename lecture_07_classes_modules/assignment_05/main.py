# [BONUS] Create the module circus.py with two classes:
# - Elephant – attributes name, weight and the method is_too_heavy that will return True if the
# elephant is heavier than 8 tons.
# - Lion – attributes name, age, methods is_too_old that will return True if the lion is older than 5 years.
# Module will contain two functions:
# - create_random_circus() – creates a list of one random lion (random name and age) and one random elephant (random name and weight).
# - filter_animals(animals) – filters animals that are too heavy (in case of the elephants) and too old (in case of the lions).
# Import this module to main.py, where you create and print random circus, then filter animals and print animals that are left.

import circus

elephant = circus.Elephant("Snoopy",5)


print(elephant.is_too_heavy)
