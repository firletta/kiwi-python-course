# Create a recusrive function, that will for given text prints it in reversed order.

text = "Kiwi course"

# reversed_text = text [::-1]
# print(f"Reversed text: {reversed_text}")

def reverse(text):
    if len(text) == 0:
        return text
    else:
        return reverse(text[1:]) + text[0]

print(f"Reversed text: {reverse(text)}")
