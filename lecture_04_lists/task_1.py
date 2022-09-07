# Generate list of all odd numbers up to 100, then print only numbers divisible by 7

numbers =[]
for i in range(1,101):
    if i % 2 != 0:
        numbers.append(i)
        if i % 7 == 0:
            print(i)