import collections
word_to_guess = "hello"
user_guess = "stone"
results1 = collections.Counter(word_to_guess)
results2 = collections.Counter(user_guess)
print(results1)
print(results2)

print(collections.Counter(word_to_guess).keys())
print(collections.Counter(user_guess).keys())

print(collections.Counter(word_to_guess).values())
print(collections.Counter(user_guess).values())

if 2 in collections.Counter(word_to_guess).values():
    print("double")


