# [BONUS] Write a program, that will rearrange the items in the list [1, 97, 15, 82, 38, 29], so that they are sorted from the smallest number to the biggest one. You can swap two items in the list using:

# l = [1, 97, 15, 82, 38, 29]
# l[1], l[3] = l[3], l[1]
# l == [1, 82, 15, 97, 38, 29]

# You can use Selection Sort (and two [nested] for loops).

num = [1, 97, 15, 82, 38, 29]

n = len(num)

for i in range(n-1):
    current_minimum = i

    for j in range(i+1, n):
        if num[j] < num[current_minimum]:
            current_minimum = j

        if current_minimum != i:
            current_number = num[i]
            num[i] = num[current_minimum]
            num[current_minimum] = current_number

print(num)