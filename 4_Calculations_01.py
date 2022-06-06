"""this program works out the average unit price
Made by Abigael
25/05/2022
"""

# Variables
number = 0
total_price = 0
calc = float()

# Lists
test_list = [["Greggs", 200.0, 7.0], ["Moccona", 90.0, 10.49],
             ["Nescafe", 180.0, 7.79]]

# Main Routine
for index in range(len(test_list)):
    number += 1
    price_numbers = float(test_list[index][2])
    quantity_numbers = float(test_list[index][1])
    total_price += float(price_numbers)
    calc += round(price_numbers / quantity_numbers, 2)

print(f"The average unit price is ${round(calc / number, 2)}")
