orders = int(input())

total_price = 0

for i in range(orders):
    price_capsule = float(input())
    days = int(input())
    capsules = int(input())
    price = price_capsule * capsules * days
    print(f"The price for the coffee is: ${price:.2f}")
    total_price += price


print(f"Total: ${total_price:.2f}")