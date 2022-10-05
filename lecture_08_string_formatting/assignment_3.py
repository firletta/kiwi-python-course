# Create a class Car, with attributes year, horsepower, name and brand
# Implement method to print this attributes automatically
# Create any car and print it

class Car:
    def __init__(self, year, horsepower, name, brand):
        self.year = year
        self.horsepower = horsepower
        self.name = name
        self.brand = brand

    def __str__(self):
        return f"- {self.brand} - {self.name} - {self.year} - {self.horsepower} -"


car = Car("2019","200","Clio","Renault")
print(car)
