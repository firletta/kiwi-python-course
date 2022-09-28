# Create an application with the class Calculator.
# The class will have 4 methods – add, subtract, multiply, and divide.
# All methods will take two numbers as parameters. Test your calculator with the few examples.

class Calculator:
    def add(self, x, y):
        self.result = x + y
        return self.result
    def subtract(self, x, y):
        self.result = x - y
        return self.result
    def multiply(self, x, y):
        self.result = x * y
        return self.result
    def divide(self, x, y):
        self.result = x / y
        return self.result
    
calculator1 = Calculator()
calculator2 = Calculator()

add_result = calculator1.add(1,3)
multiply_result = calculator2.multiply(2, 3)

print(add_result)
print(multiply_result)

calculator1.divide(6, 3)

print(calculator1.result)
