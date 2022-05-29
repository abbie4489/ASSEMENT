"""This component will allow the user to enter the mass / volume from choice
of g, l, ml, kg
13/05/2022
Abigael
"""


def get_choice(choice):
    valid_choices = [["g", "gram", "grams"], ["l", "litre", "litres"],
                     ["ml", "milliliters", "milliliter"],
                     ["kg", "kilogram", "kilograms"]]
    choice_error = "Sorry that is not a valid choice "
    for list_item in valid_choices:
        if choice in list_item:
            print("valid answer")
            return choice
    print(choice_error)
    return


choice = get_choice(input("What unit would you like to use? "))
