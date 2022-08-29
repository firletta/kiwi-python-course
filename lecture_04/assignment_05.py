# TODO
# [BONUS] Write a program, that will rearrange the items in the list [1, 97, 15, 82, 38, 29], so that they are sorted from the smallest number to the biggest one. You can swap two items in the list using:

# l = [1, 97, 15, 82, 38, 29]
# l[1], l[3] = l[3], l[1]
# l == [1, 82, 15, 97, 38, 29]

# You can use Selection Sort (and two [nested] for loops).

num = [1, 97, 15, 82, 38, 29]

for i in range(len(num)-1):
        print(num[i], num[i+1])
        
        # if num[i] > num[i+1]:
        #   num[i], num[i+1] = num[i+1], num[i]