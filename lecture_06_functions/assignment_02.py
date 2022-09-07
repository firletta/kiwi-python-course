# Create an application with the function to compute factorial. Compute 12!, 25!, 50! and 180!

import math

numbers = [12, 25, 50, 180]

def fact(number):
	return math.factorial(number)

for number in numbers:
	print(fact(number))
