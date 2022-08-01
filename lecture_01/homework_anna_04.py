# Ask user to input 2 numbers, generate 3 random EVEN numbers between these two and then create a number that
# consists of these three numbers concatenated.
# Example: from 4, 6, 16 will create a number 4616

input_number_one = int(input("Enter first number: "))
input_number_two = int(input("Enter second number: "))

if input_number_one > input_number_two:
    number_one = input_number_two
    number_two = input_number_one
else:
    number_one = input_number_one
    number_two = input_number_two
    
if input_number_one % 2 != 0 and input_number_two == input_number_one:
    print("There is no even number between",input_number_one,"and",input_number_one)
else:
    import random
        
    number_a = random.randint(number_one,number_two)
    number_b = random.randint(number_one,number_two)
    number_c = random.randint(number_one,number_two)

    while(number_a % 2 != 0):
        number_a = random.randint(number_one,number_two)
        if number_a % 2 == 0: break
            
    while(number_b % 2 != 0):
        number_b = random.randint(number_one,number_two)
        if number_b % 2 == 0: break
            
    while(number_c % 2 != 0):
        number_c = random.randint(number_one,number_two)
        if number_c % 2 == 0: break
    print("Generated number: ",number_a,number_b,number_c, sep="")