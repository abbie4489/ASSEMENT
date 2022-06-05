"""This program adds the product, mass/volume and price to a list
called information_list. I also rounded the price and unit to 2 decimals
23/05/2022
Abigael Ward
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


# lists
information_list = []

# main routine
while True:
    product = input("Please enter the product name or press x to leave: ")
    if product != "x":
        mass = float_checker("Please enter the mass/volume of the product: ")
        price = float_checker("Please enter the price of the product: ")
        # Rounds the mass and price to 2 decimal places
        information = [product, float("%.2f" % mass), float("%.2f" % price)]
        information_list.append(information)  # adding to the list
        print(information_list)
    elif product == "x":
        print("You have left the program")
        break  # stops the while loop
