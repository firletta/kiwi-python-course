# Implement function to compute the sum of numbers in the list
# Use recursion.

def recursive_list_sum(l: [float]) -> float:
    if len(l)==0:
        return 0
    else:
        return l[0] + recursive_list_sum(l[1:])

l = [1, 5, 7, 9, 4, 1, 2, 5]
print(recursive_list_sum(l) == sum(l))
