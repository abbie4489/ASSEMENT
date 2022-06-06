"""This component will allow the user to enter the mass / volume from choice
of g, l, ml, kg
24/05/2022
Abigael
"""

# Lists
valid_choices = [["g", "gram", "grams"], ["l", "litre", "litres"],
                 ["ml", "milliliters", "milliliter"],
                 ["kg", "kilogram", "kilograms"]]

# main component
choice = input("What unit would you like to use? ")

# determines if its valid answer or not
for list_item in valid_choices:
    if choice not in list_item:
        print("invalid answer")
        break
    else:
        print("valid answer")
        break


