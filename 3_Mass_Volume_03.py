"""This component will allow the user to enter the mass / volume from choice
of g, l, ml, kg but this time with error message
25/05/2022
Abigael
"""


# Functions
def get_choice(unit):
    valid_choices = [["g", "gram", "grams"], ["l", "litre", "litres"],
                     ["ml", "milliliters", "milliliter"],
                     ["kg", "kilogram", "kilograms"]]
    choice_error = "Sorry that is not a valid choice "
    for list_item in valid_choices:
        if unit in list_item:
            print("valid answer")
            return unit
    print(choice_error)  # if unit not in list
    return


# Main routine
unit = get_choice(input("What unit would you like to use? "))
