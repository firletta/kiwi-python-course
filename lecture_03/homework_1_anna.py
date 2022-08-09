# Write a program that will compute an average of numbers between two given numbers.
# User will specify minimum and maximum number.
# Your application will compute the average of all numbers between these two numbers.
# Bouns - try to do it with both for & while loop

input_number_one = int(input("Enter a number: "))
input_number_two = int(input("Enter another number: "))

if input_number_one > input_number_two:
    number_start = input_number_two +1
    number_end = input_number_one
else:
    number_start = input_number_one +1
    number_end = input_number_two

numbers = []

if (number_start - 1) == number_end:
    print("The numbers are the same.")
elif number_start == number_end:
    print(f"There are no whole numbers in between {number_start - 1} and {number_end}.")
else:
    for i in range(number_start,number_end):
        numbers.append(i)
    # BONUS:
    # while number_start < number_end:
        # numbers.append(number_start)
        # number_start += 1
    average = sum(numbers) / len(numbers)
    print(f"Average of numbers in between is {average}.")