# Print the given table, with the rows and columns, so they are nicely aligned
# Example of the output could look like:
# #-----------#----------------#------------#
# |  Country  |  Capital city  | Population |
# #-----------#----------------#------------#
# |Czechia    |Prague          | 10,650,000 |
# |Slovakia   |Bratislava      | 5,450,000  |
# |USA        |Washington, D.C.|327,200,000 |
# |Madagascar |Antananarivo    | 25,570,000 |
# #-----------#----------------#------------#

table = [
    # -- table header --
    ["Country", "Capital city", "Population"],
    # -- table rows --
    ["Czechia", "Prague", 10650000],
    ["Slovakia", "Bratislava", 5450000],
    ["USA", "Washington, D.C.", 327200000],
    ["Madagascar", "Antananarivo", 25570000],
]

def separator():
    return print(f"#{'-'*12}#{'-'*18}#{'-'*14}#")

separator()
print(f"|{table[0][0]:^12}|{table[0][1]:^18}|{table[0][2]:^14}|")
separator()
for rows in table[1:5]:
    print(f"|{rows[0]:<12}|{rows[1]:<18}|{rows[2]:>14,}|")
separator()