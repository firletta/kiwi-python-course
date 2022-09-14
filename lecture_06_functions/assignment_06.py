# Create a function to compute factorial recursively

def fact(n):
    print(n)
    if n == 1:
        return n

    return n * fact(n - 1)

num = 5

print(fact(num))
