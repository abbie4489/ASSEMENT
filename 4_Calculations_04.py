"""Average Price, Best value = price / quantity and the most expensive item,
cheapest item
29/05/2022
Abigael
"""

calc = float()
number = 0
total_price = 0
cheapest_item, cheapest_value = float(), float()
expensive_item, expensive_item_value = float(), float()
test_list = [["coffee", "200", "70"], ["Moccona", "90", "10"],
             ["Nescafe", "180", "7.79"]]

for index in range(len(test_list)):
    number += 1
    price_numbers = float(test_list[index][2])
    total_price += float(price_numbers)
    quantity_numbers = float(test_list[index][1])
    value = round(price_numbers / quantity_numbers, 2)
    calc += round(price_numbers / quantity_numbers, 2)
    if value > cheapest_value:
        cheapest_item, cheapest_value = (test_list[index][0]), value
    elif value > expensive_item_value:
        expensive_item, expensive_item_value = (test_list[index][0]), value

print(f"Average unit price: ${round(calc / number, 2)}\nCheapest "
      f"item: {cheapest_item} with the price of ${cheapest_value} per unit"
      f"\nMost expensive item: {expensive_item} with the price of "
      f"{expensive_item_value} per unit")
