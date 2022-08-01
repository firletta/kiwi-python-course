# Ask user to fill in his weight (kgs) and height (cm) and compute his/her BMI and print it back
import math
weight = float(input("Enter your weight in kg: "))
height = float(input("Enter your height in cm: "))
bmi = round((weight / (height/100)**2), 2)
print("Your BMI is",bmi)