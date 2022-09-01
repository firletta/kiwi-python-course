# Create a function check_city, that will take a county and city as a parameter
# The function will look into geomap if the city is in given country
# Then it will say, if the city is in given country or not

geomap = {
    "UK": ["London", "Manchester", "Liverpool"],
    "Czech Republic": ["Prague", "Brno", "Ostrava"],
    "Slovak Republic": ["Bratislava", "Košice"],
    "USA": ["Washington", "New York", "Detroit"],
    "Germany": ["Berlin", "Hamburg", "Munich"]
}

def check_city(country, city):
    my_list = geomap.get(country, [])
    if city in my_list:
        return True
    else:
        return(False)

print(check_city("Australia", "Brno"))
