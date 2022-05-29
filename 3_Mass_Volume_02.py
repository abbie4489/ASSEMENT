"""This component will allow the user to enter the mass / volume from choice
of g, l, ml, kg
13/05/2022
Abigael
"""

valid_choices = [["g", "gram", "grams"], ["l", "litre", "litres"],
                 ["ml", "milliliters", "milliliter"],
                 ["kg", "kilogram", "kilograms"]]
choice = input("What unit would you like to use? ")

for list_item in valid_choices:
    if choice not in list_item:
        print("invalid answer")
        break
    else:
        print("Sorry that is not a valid choice")
        break


