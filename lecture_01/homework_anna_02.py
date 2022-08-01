# Ask user for 2 numbers and generate random (whole) number between those two numbers

number_a = int(input("Enter a number: "))
number_b = int(input("Enter another number: "))
import random
if number_a < number_b:
    generated_number = random.randint(number_a,number_b)
if number_a > number_b:
    generated_number = random.randint(number_b, number_a)
print("Random number between them:", generated_number)