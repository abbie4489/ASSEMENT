"""converts ml into l and kg into g
Made by Abigael
5/06/2022
"""


# Functions
# make sure that the number is less than zero
def number_checker(num):
    valid_num = True
    if num < 0:
        valid_num = False
    return valid_num


# Make sure that it is a float and if not then it repeats the question
def float_checker(question):
    error = "\nSorry, that is not a valid choice\n"  # if its not a integer
    while True:
        try:
            element = float(input(question))  # re asks the question
            return element
        except ValueError:
            print(error)  # prints error message here


# Splits the mass
def get_choice(mass):
    # list
    valid_choices = [["g", "gram", "grams"], ["kg", "kilogram", "kilograms"],
                     ["l", "litre", "litres"],
                     ["ml", "milliliters", "milliliter"]]
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

    if not number_checker(number):
        valid_num = True

    number = str(number)
    first_number = number[0]
    if first_number == "-":
        is_error = True

    if is_error:
        print(choice_error)
        return

    # breaking down the list
    for list_item in valid_choices:
        for unit_label in list_item:
            if unit_label == unit:
                print(f"unit: {unit}\nNumber: {number}")
                if unit in valid_choices[0]:
                    correct_unit_price = number, "Grams"
                elif unit in valid_choices[1]:
                    correct_unit_price = number * 1000, "Grams"
                elif unit in valid_choices[3]:
                    correct_unit_price = number / 1000, "Litres"
                elif unit in valid_choices[2]:
                    correct_unit_price = number, "Litres"
                print(correct_unit_price)
                result = correct_unit_price
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

        valid_num = False
        while not valid_num:
            price = float_checker("Please enter the price of the product: ")
            valid_num = number_checker(price)
        # Rounds the mass and price to 2 decimal places
        information = [product, float("%.2f" % 3), float("%.2f" % price)]
        information_list.append(information)  # adding to the list
        print(information_list)
    elif product == "x":
        print("You have left the program")
        break  # stops the while loop
