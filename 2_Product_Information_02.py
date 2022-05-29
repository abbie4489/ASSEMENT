""" This program adds on from product loop 2
Abigael
"""

product = ""
while True:
    product = input("Please enter the product or press x to leave: ").title()
    if product != "X":
        print(product)
    else:
        print("You have left the program")
        break

