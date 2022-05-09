initial = input()
products = dict()

while initial != "statistics":
    initial = initial.split(": ")
    product = initial[0]
    quantity = int(initial[1])
    if product not in products:
        products[product] = 0
    products[product] += quantity
    initial = input()

print(f"Products in stock:")
for (product, quantity) in products.items():
    print(f"- {product}: {quantity}")
print(f"Total Products: {len(products.keys())}")
print(f"Total Quantity: {sum(products.values())}")


