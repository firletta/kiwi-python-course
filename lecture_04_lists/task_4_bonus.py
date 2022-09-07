# Try to implement Selection Sort. Mechanism for sorting the list of numbers
# as an input use [41, 13, 5, -5, 9, 0, 0, 41, -1, -23, 0]
# or for testing purposes use generate a list of random numbers (lets say -100 to 100) and then print the sorted result.
# as an explanation check https://www.youtube.com/watch?v=g-PGLbMth_g
# or https://www.youtube.com/watch?v=Z3dCjzhjAWA
# (don't look at the solution at the end of videos, it wouldn't be fun otherwise)

the_list = [41, 13, 5, -5, 9, 0, 0, 41, -1, -23, 0]

n = len(the_list)

for i in range(n-1):
    current_minimum = i

    for j in range(i+1, n):
        if the_list[j] < the_list[current_minimum]:
            current_minimum = j

        if current_minimum != i:
            current_number = the_list[i]
            the_list[i] = the_list[current_minimum]
            the_list[current_minimum] = current_number

print(the_list)