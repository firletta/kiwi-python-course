# Create a class Temperature which contains the temperature value and unit
# class should have 3 methods: convert_to_kelvins, convert_to_celsius, convert_to_fahrenheit
# calling each method should result in re-computation of the value in Temperature class and assigning correct unit.

class Temperature:
    def convert_to_kelvins(self, value, unit):
        if unit == "C":
            self.result = value + 273.15
        elif unit == "F":
            self.result = (value - 32) * 5 / 9 + 273.15
        return str(self.result) + "K"
    def convert_to_celsius(self, value, unit):
        if unit == "K":
            self.result = value - 273.15
        elif unit == "F":
            self.result = (value - 32) * 5 / 9
        return str(self.result) + "C"
    def convert_to_fahrenheit(self, value, unit):
        if unit == "C":
            self.result = 9 / 5 * value + 32
        elif unit == "K":
            self.result =  9 / 5 * (value - 273)
        return str(self.result) + "F"

temperature_converter = Temperature()

temp1 = temperature_converter.convert_to_kelvins(20, "C")
temp2 = temperature_converter.convert_to_celsius(293.15, "K")
temp3 = temperature_converter.convert_to_fahrenheit(20, "C")
print(temp1, temp2, temp3)

