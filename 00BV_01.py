"""Components 1_User_Budget_03.py and 2_Product_Information_04"""

# Functions:
def float_checker(question):
    error = "\nSorry, that is not a valid choice\n"  # if its not a integer
    while True:
        try:
            floater = float(input(question))
            return floater
        except ValueError:
            print(error)


# lists
information_list = []

# main routine
budget = float_checker("What is the maximum amount you want to spend? ")
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
