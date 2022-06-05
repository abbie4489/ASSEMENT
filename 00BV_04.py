"""Adding component 5_Recommendation_03.py - Identifying the price that is the
lowest below the budget make the recommendation. version 2
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


# function that ends when appropriate answer is entered
def get_budget():
    cheapest_item = min(information_list, key=lambda x: x[2])
    cheaper = cheapest_item[2]
    print(f"The cheapest price is ${cheaper}")
    budget = 0
    valid = False
    while not valid or budget < cheaper:
        try:
            budget = float(input('what is your budget? (please enter budget '
                                 'above lowest price): '))
        except ValueError:
            print('not a valid response')
        else:
            valid = True
    return budget


def best_value(information_list, budget):
    affordable = [item for item in information_list if item[2] <= budget]
    max_affordable = []
    for i in range(0, len(affordable)):
        if i == 0:
            max_affordable = affordable[i]
        elif affordable[i][3] < max_affordable[3]:
            max_affordable = affordable[i]
        elif affordable[i][3] == max_affordable[3]:
            max_affordable.append(affordable[i])

    return max_affordable



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

budget = get_budget()
value = best_value(information_list, budget)
# Recommendation
print("The item with the best value for you is", '{}, {}, {}'.format(value[0],
                                                                     value[1],
                                                                     value[2]))
