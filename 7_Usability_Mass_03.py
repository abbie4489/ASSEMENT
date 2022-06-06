"""This component This program recognises the number and the unit then splits
them into different variables and gives a error message that is more
efficient /logical
Made by Abigael
5/06/2022
"""


# Functions
# Make sure that it is a float and if not then it repeats the question
def float_checker(question):
    error = "\nSorry, that is not a valid choice\n"  # if its not a integer
    while True:
        try:
            element = float(input(question))  # re asks the question
            return element
        except ValueError:
            print(error)  # prints error message here


# function
# Splits the mass
def get_choice(mass):
    # list
    valid_choices = [["g", "gram", "grams"], ["l", "litre", "litres"],
                     ["ml", "milliliters", "milliliter"],
                     ["kg", "kilogram", "kilograms"]]
    choice_error = "Please enter in the format of amount and unit eg. 10g"
    result = False
    mass = input("Please enter the mass/volume of the product: ")

    split = 0
    # Splitting the number and string
    for i in range(0, len(mass)):
        if mass[i].isdigit():
            split = i
    number = mass[:split + 1]
    unit = mass[split + 1:]

    # Loop to get appropriate answer for mass
    is_error = False
    try:
        number = float(number)
    except ValueError:
        is_error = True

    if not number or not unit:
        is_error = True
        print("d")

    if is_error:
        print('error')

    # breaking down the list
    for list_item in valid_choices:
        for unit_label in list_item:
            if unit_label == unit:
                result = unit
                print(f"unit: {unit}\nNumber: {number}")
    if not result:
        print(choice_error)

    return result


# lists
information_list = []

# Main routine

# main routine
while True:
    product = input("Please enter the product name or press x to leave: ")
    if product != "x":
        mass = False
        while not mass:
            mass = get_choice(mass)
        # mass = float_checker("Please enter the mass/volume of the product: ")
        price = float_checker("Please enter the price of the product: ")
        # Rounds the mass and price to 2 decimal places
        information = [product, float("%.2f" % 3), float("%.2f" % price)]
        information_list.append(information)  # adding to the list
        print(information_list)
    elif product == "x":
        print("You have left the program")
        break  # stops the while loop
