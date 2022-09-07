countries = {
    "Prague": "Czech Republic",
    "Paris": "France",
    "Warsaw": "Poland",
}
chosen_city = input("Enter a city: ")
if chosen_city in countries.keys():
    print("It is located in " + countries[chosen_city])
else:
    print("City doesn't exist")
    
# another way to do it is with get function and None value