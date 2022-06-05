"""This component loops the questions mass / volume until a valid answer
13/05/2022
Abigael
"""


# function
def get_choice(choice):
    # list
    valid_choices = [["g", "gram", "grams"], ["l", "litre", "litres"],
                     ["ml", "milliliters", "milliliter"],
                     ["kg", "kilogram", "kilograms"]]
    choice_error = "Sorry that is not a valid choice "
    result = False
    choice = input("What unit would you like to use? ")
    # breaking down the list
    for list_item in valid_choices:
        for unit in list_item:
            if unit == choice:
                result = choice
    if not result:
        print(choice_error)
    return result


# Main routine
choice = False
while not choice:
    choice = get_choice(choice)
print(choice)
