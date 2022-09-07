# Create two lists of 10 random numbers (int) between 0 and 20,
# print both of them. Create third list that contain only numbers from the first list that are in both lists.
# example:
# list1 = [4, 3, 12, 6, 2, 9, 5, 5, 14, 19]
# list2 = [3, 5, 0, 10, 11, 10, 17, 9, 2, 0]
# result = [3, 2, 9, 5, 5]

# Note from Anna: Just for fun I also wanted to make it so the numbers will not repeat in the lists

import random

list1 = []
list2 = []
result = []

for i in range(10):
    random_number = random.randint(0,20)
    while True:
        if random_number in list1:
            random_number = random.randint(0,20)
        else:
            list1.append(random_number)
            break

for i in range(10):
    random_number = random.randint(0,20)
    while True:
        if random_number in list2:
            random_number = random.randint(0,20)
        else:
            list2.append(random_number)
            break

for number in range(len(list1)):
    if list1[number] in list2:
        result.append(list1[number])

print(list1)
print(list2)
print(result)