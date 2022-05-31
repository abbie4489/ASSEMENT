"""Average Price, cheapest item
29/05/2022
Abigael
"""
calc = float()
number = 0
total_price = 0
best_value_price = float()
cheapest_item = float()
test_list = [["coffee", "200", "7"], ["Moccona", "90", "10"],
             ["Nescafe", "180", "7.79"]]

for index in range(len(test_list)):
    number += 1
    price_numbers = float(test_list[index][2])
    total_price += float(price_numbers)
    quantity_numbers = float(test_list[index][1])
    value = round(price_numbers / quantity_numbers, 2)
    calc += round(price_numbers / quantity_numbers, 2)
    if value > best_value_price:
        best_value_price = value
        cheapest_item = (test_list[index][0])

print(f"The average unit price is ${round(calc / number, 2)}\nThe cheapest "
      f"item is {cheapest_item} with the price of ${best_value_price} per gram")
