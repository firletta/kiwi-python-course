# Create an application with the class TimeConverter and the attribute seconds.
# Add 3 methods print_seconds, print_minutes, and print_hours that will print
# how many seconds/minutes/hours are in the given number of seconds.

class TimeConverter:
    def __init__(self, number_of_seconds):
        self.number_of_seconds = number_of_seconds
    
    def print_seconds(self):
        print(self.number_of_seconds)
    
    def print_minutes(self):
        number_of_minutes = self.number_of_seconds // 60
        print(number_of_minutes)
    
    def print_hours(self):
        number_of_hours = self.number_of_seconds // 3600
        print(number_of_hours)
        
time_converter_500 = TimeConverter(500)
time_converter_7854 = TimeConverter(7854)

time_converter_500.print_seconds()
time_converter_7854.print_seconds()

time_converter_500.print_minutes()
time_converter_7854.print_minutes()

time_converter_500.print_hours()
time_converter_7854.print_hours()