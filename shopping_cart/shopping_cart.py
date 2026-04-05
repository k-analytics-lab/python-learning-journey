items = []
prices = []
total = 0

while True:
    item = input("Enter the item you want to buy (press q to quit): ")
    if item.lower() == "q":
        break
    else:
        price = int(input(f"Enter the price of {item}: $"))
        items.append(item)
        prices.append(price)

print()
print(5*"-","Shopping List",5*"-")

for item,price in zip(items,prices):
    print(f"{item} - ${price}")
    total += price

print(f"The total price is: ${total}")