number_of_items = int(input("Number of items: "))
price = 0

while number_of_items <= 0:
    print("Invalid number of items")
    number_of_items = int(input("Number of items: "))
for i in range(number_of_items):
    item_price = float(input("Price of item: "))
    price = price + item_price

if price > 100:
    price *= 0.9
    print("Total price for {} items is ${:.2f}".format(number_of_items, price))
else:
    print("Total price for {} items is ${:.2f}".format(number_of_items, price))
