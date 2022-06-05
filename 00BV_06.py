"""Adding component 6_Display_03
"""

# import the library
import pandas as pd


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


should_continue = True
while should_continue:
    print("### Welcome to Best Value ###\n")
    print("This program will take the product name, weight \nprice to recommend "
          "what product you should buy")
    print("--The unit is the weight unit e.g. kg, g, ml, l \n")
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
          f"item: {cheapest_item[0]}\nMost expensive item: {expensive_item[0]}")
    print("__________________________________")
    budget = get_budget()
    value = best_value(information_list, budget)
    # Recommendation
    print("------------------------------------------------------------------")
    print("The item with the best value for you is", '{}, {}, {}'.format(value[0],
                                                                         value[1],
                                                                         value[2]))
    print("------------------------------------------------------------------")
    print("\n\n")
    # sorting the original list
    information_list.sort(key=lambda row: (row[3]))

    # new list with headers and pandas format
    displayed_list = pd.DataFrame({'Name': [item[0] for item in information_list],
                                   'Weight': [item[1] for item in information_list],
                                   'Price$': [item[2] for item in information_list],
                                   'Value$': [item[3] for item in information_list]})

    displayed_list.to_csv("ticket_details.csv")

    # print statements
    print(displayed_list)

    exit = input("\npress enter to exit and anything else to continue")
    if exit == "":
        should_continue = False
