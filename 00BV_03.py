"""Adding component 4_Calculations_06.py this component asks for the
Best value = price / quantity and the most expensive item, cheapest item,
adding the value to the list and then sorting the list. let the user add
the information to the list.
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
total_value = float()
total_price = float()
cheapest_item, cheapest_value = float(), float()
expensive_item, expensive_item_value = float(), float()

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
        break  # stops the while loop

# Sorts the list by price
information_list = sorted(information_list, key=lambda x: x[2])

for index in range(0, len(information_list)):
    value = round(float((information_list[index][2]) / (information_list[index][1])), 2)
    total_price += float(information_list[index][2])
    total_value += round(float(information_list[index][2]) / float(information_list[index][1]), 2)
    information_list[index].append(value)
    cheapest_item = information_list[0]
    expensive_item = information_list[-1]

# Print Statements
print(f"Average unit price: ${round(total_value / len(information_list), 2)}\nCheapest "
      f"item: {cheapest_item[0]} with the price of ${cheapest_item[3]} per unit"
      f"and a overall price of ${cheapest_item[2]}\nMost expensive item: "
      f"{expensive_item[0]} with the price of ${expensive_item[3]} per unit and"
      f" a overall price of ${expensive_item[2]}")
