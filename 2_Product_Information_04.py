"""This program adds on to 2_product_information_04 and adds the product, unit
and price to a list called information_list. I also rounded the price and unit
23/05/2022
Abigael Ward
"""


def float_checker(question):
    error = "\nSorry, that is not a valid choice\n"  # if its not a integer
    while True:
        try:
            element = float(input(question))
            return element
        except ValueError:
            print(error)  # prints error message here


# lists
information_list = []
# main routine
while True:
    product = input("Please enter the product name or press x to leave: ")
    if product != "x":
        unit = float_checker("Please enter the mass/volume of the product: ")
        price = float_checker("Please enter the price of the product: ")
        information = [product, float("%.2f" % unit), float("%.2f" % price)]
        information_list.append(information)
        print(information_list)
    elif product == "x":
        print("You have left the program")
        break
