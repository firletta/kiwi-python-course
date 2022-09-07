#TODO
# Create a function that will for given list of integers compute the number of occurrences of 1 and returns it
# Print the number of 1's in given list of numbers

# -- BONUS 1 --
# Adapt the function to be able to count the occurrence of every number (not just one)
# The function will return a dictionary, where the key is a number and the value is the number of times the number is in list
# For example for the list below, the output will be:

# -- BONUS 2 --
# Adapt the function to work with list of words

numbers = [7, 1, 5, 8, 9, 1, 1, 4, 3, 1, 2, 0]

words = ["this", "is", "a", "simple", "text", "where", "we", "count", "a", "frequency", "of", "words", "within", "it", "it", "is", "useful", "for", "frequency", "analysis"]

def how_many(numbers: list):
    count = 0
    for i in numbers:
        if i == 1:
            count += 1
	return count
result = how_many(numbers=numbers)
print(result)
