"""adding component 3_mass_volume_04 This component loops the questions mass /
volume until a valid answer
"""


# Functions:
def float_checker(question):
    error = "\nSorry, that is not a valid choice\n"  # if its not a integer
    while True:
        try:
            floater = float(input(question))
            return floater
        except ValueError:
            print(error)


def get_choice(choice):
    valid_choices = [["g", "gram", "grams"], ["l", "litre", "litres"],
                     ["ml", "milliliters", "milliliter"],
                     ["kg", "kilogram", "kilograms"]]
    choice_error = "Sorry that is not a valid choice "
    result = False
    choice = input("What unit would you like to use? ")
    for list_item in valid_choices:
        for unit in list_item:
            if unit == choice:
                result = choice
    if not result:
        print(choice_error)
    return result


# lists
information_list = []

# Variables


# main routine
choice = False
while not choice:
    choice = get_choice(choice)
print("the unit you are using is", choice)

budget = float_checker("What is the maximum amount you want to spend? ")
while True:
    product = input("\nPlease enter the product name or press x to leave: ")
    if product != "x":
        unit = float_checker("Please enter the mass/volume of the product: ")
        price = float_checker("Please enter the price of the product: ")
        information = [product, float("%.2f" % unit), float("%.2f" % price)]
        information_list.append(information)
    elif product == "x":
        print("\n----------------------------")
        print("You have left the program")
        print("----------------------------\n")
        break
