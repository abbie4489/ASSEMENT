"""This program asks for the volume/mass and the price of the product
Abigael
"""


def information(question):
    if question == "x":
        print("You have left the program")
        return False
    else:
        return question


# main routine
while True:
    information(input("Please enter the product name or press x to leave: "))
    information(input("Please enter the mass/volume of the product: "))
    information(input("Please enter the price of the product: "))
