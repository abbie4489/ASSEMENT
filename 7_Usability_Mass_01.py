"""This program recognises the number and the unit then splits them into
different variables
Made by Abigael
5/06/2022
"""

mass = input("Enter Mass:")

# Splitting the number and string
for item, c in enumerate(mass):
    if not c.isdigit():
        break

# Variables
number = int(mass[:item])
unit = mass[item:]

# Print statement
print(number)
print(unit)
