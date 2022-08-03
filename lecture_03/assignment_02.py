user_number = int(input("Plesae enter number grater then 0: "))

if user_number < 0:
    print("This number is not correct")
    exit()
    
factorial = 1
for i in range(1,user_number+1):
    factorial = factorial * i
    print(factorial)
    

