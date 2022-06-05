"""This component will allow the user to enter the unit they want to use for
the mass
13/05/2022
Abigael
"""
# lists
valid_choices = [["g", "gram", "grams"], ["l", "litre", "litres"],
                 ["ml", "milliliters", "milliliter"],
                 ["kg", "kilogram", "kilograms"]]

# main component
choice = input("What unit would you like to use? ")

# determines if its valid answer or not
for list_item in valid_choices:
    if choice in list_item:
        print("This is a valid answer")
