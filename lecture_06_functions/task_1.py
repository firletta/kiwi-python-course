# Implement a function merge_routes, that takes two arguments (strings) route_1 & route_2
# Each route is a string of a format [IATA]->[IATA]->[IATA]
# The function will return the merged route if the final destination of route_1 is equal to initial destination of route_2
# The function will return None if the destinations of route_1 & route_2 don't match
#
# Examples
# - merge_routes("JFK->LHR->PRG", "PRG->VIE") == "JFK->LHR->PRG->VIE"
# - merge_routes("JFK->LHR->PRG", "FCO->VIE") == None
#
# You can use helper functions .split(), .join() explained in the code below
from __future__ import annotations # no need for this if REPL would be in python 3.10


def merge_routes(route_1: str, route_2: str) -> str | None:
    route_1_list = route_1.split("->")
    route_2_list = route_2.split("->")
    if route_1_list[-1] == route_2_list[0]:
        del route_2_list[0]
        route = "->".join(route_1_list + route_2_list)
    else:
        route = None
    return route


route_1 = "JFK->LHR->PRG"
# print(route_1.split("->")) # you can use split function to get a list of individual cities
# print("->".join(["JFK", "LHR", "PRG"])) # you can use join function to construct route from list of cities
route_2 = "PRG->VIE"
route_3 = "FCO->VIE"

print(merge_routes(route_1, route_2) == "JFK->LHR->PRG->VIE")
print(merge_routes(route_1, route_3) == None)
