# Ask user for a real number, padding_width and precision.
# Print the number using with given padding_width and precision

number = float(input("Please enter a number: "))
padding_width = int(input("Please enter padding width: "))
precision = int(input("Please enter precision: "))

print(f"#{number:^{padding_width}.{precision}f}#")