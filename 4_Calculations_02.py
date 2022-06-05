"""this program works out the most expensive item per unit
Abigael
"""

# Variables
calc = float()
number = 0
total_price = 0
expensive_item, expensive_item_value = float(), float()

# Lists
test_list = [["Greggs", 200.0, 7.0], ["Moccona", 90.0, 10.49],
             ["Nescafe", 180.0, 7.79]]

# Main Routine
for index in range(len(test_list)):
    number += 1  # how many items in the list their are
    price_numbers = float(test_list[index][2])
    total_price += float(price_numbers)
    quantity_numbers = float(test_list[index][1])
    value = round(price_numbers / quantity_numbers, 2)
    calc += round(price_numbers / quantity_numbers, 2)
    if value > expensive_item_value:
        expensive_item, expensive_item_value = (test_list[index][0]), value

# Print statement
print(f"Average unit price: ${round(calc / number, 2)}"
      f"\nMost expensive item: {expensive_item} with the price of "
      f"{expensive_item_value} per unit")
