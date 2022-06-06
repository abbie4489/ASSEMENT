"""Adding component 6_Display_03
made by Abigael
6/06/2022
"""

# import the library
import pandas as pd
import csv


# Functions:
def get_number(num):
    valid_num = True
    if num < 0:
        valid_num = False
    return valid_num


# Checks if the input is a float if not theirs error
def get_float(question):
    error = "\nSorry, that is not a valid choice\n"  # if its not a integer
    while True:
        try:
            element = float(input(question))  # re asks the question
            return element
        except ValueError:
            print(error)     # prints error message here


# splits the mass onto two variables
def get_choice(mass):
    # list
    valid_choices = [["G", "Gram", "Grams"], ["Kg", "Kilogram", "Kilograms"],
                     ["L", "Litre", "Litres"],
                     ["Ml", "Milliliters", "Milliliter"]]
    choice_error = "Please enter in the format of amount and unit eg. 10g"
    result = False
    mass = input("Please enter the mass/volume of the product: ")
    split = 0
    # Splitting the number and string
    for i in range(0, len(mass)):
        if mass[i].isdigit():
            split = i
    number = mass[:split + 1]
    unit = mass[split + 1:].capitalize()

    # Loop to get appropriate answer for mass
    is_error = False
    try:
        number = float(number)
    except ValueError:
        is_error = True
    else:
        if not get_number(number):
            is_error = True

    if not number or not unit:
        is_error = True



    correct_unit_price = 0
    for list_item in valid_choices:
        for unit_label in list_item:
            if unit_label == unit:
                if unit in valid_choices[0]:
                    correct_unit_price = number, "Grams"
                elif unit in valid_choices[1]:
                    correct_unit_price = number * 1000, "Grams"
                elif unit in valid_choices[3]:
                    correct_unit_price = number / 1000, "Litres"
                elif unit in valid_choices[2]:
                    correct_unit_price = number, "Litres"
                result = correct_unit_price

    if is_error:
        result = False
    if not result:
        print(choice_error)

    print(number)
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


# returns the most affordable item
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
valid_choices = [["g", "gram", "grams"], ["kg", "kilogram", "kilograms"],
                 ["l", "litre", "litres"],
                 ["ml", "milliliters", "milliliter"]]

# Variables
total_value = float()
total_price = float()
cheapest_item, cheapest_value = float(), float()
expensive_item, expensive_item_value = float(), float()

should_continue = True
while should_continue:
    print("### Welcome to Best Value ###\n")
    print("This program will take the product name, weight \nprice to "
          "recommend what product you should buy")
    print("--The unit is the weight unit e.g. kg, g, ml, l \n")

    # main routine
    while True:
        product = input("Please enter the product name or press x to leave: ")
        if product != "x":
            mass = False
            while not mass:
                mass = get_choice(mass)
            number, unit = mass
            valid_num = False
            while not valid_num:
                price = get_float("Please enter the price of the product: ")
                valid_num = get_number(price)
                # Rounds the mass and price to 2 decimal places
                information = [product, float("%.2f" % number), float("%.2f" % price)]
                information_list.append(information)  # adding to the list

        elif product == "x":
            print("\n###Results###")
            break  # stops the while loop

    # Sorts the list by price
    information_list = sorted(information_list, key=lambda x: x[2])

    for index in range(0, len(information_list)):
        value = round(float((information_list[index][2]) /
                      (information_list[index][1])), 2)
        total_price += float(information_list[index][2])
        total_value += round(float(information_list[index][2]) /
                             float(information_list[index][1]), 2)
        information_list[index].append(value)
        cheapest_item = information_list[0]
        expensive_item = information_list[-1]

    # Print Statements
    print(f"Average unit price: "
          f"${round(total_value / len(information_list), 2)}\nCheapest item: "
          f"{cheapest_item[0]}\nMost expensive item: {expensive_item[0]}")
    print("__________________________________")
    budget = get_budget()
    value = best_value(information_list, budget)
    # Recommendation
    print("------------------------------------------------------------------")
    print("The item with the best value for you is",
          '{}, {}, {}'.format(value[0], value[1], value[2]))
    print("------------------------------------------------------------------")
    print("\n\n")
    # sorting the original list
    information_list.sort(key=lambda row: (row[3]))

    # new list with headers and pandas format
    displayed_list = pd.DataFrame(
        {'Name': [item[0] for item in information_list],
         'Weight': [item[1] for item in information_list],
         'Price$': [item[2] for item in information_list],
         'Value$': [item[3] for item in information_list]})

    displayed_list.to_csv("ticket_details.csv")

    # print statements
    print(displayed_list)

    # excel sheet
    with open('Best_Value.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["Name", "Weight", "Price", 'Value'])
        writer.writerows(information_list)

    exit = input("\npress enter to exit and anything else to continue")
    if exit == "":
        should_continue = False
