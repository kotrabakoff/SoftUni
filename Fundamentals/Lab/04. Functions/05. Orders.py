def Total_price(product, quantity):
    if product == "coffee":
        total = quantity * 1.50
        return round(total, 2)
    elif product == "water":
        total = quantity * 1.00
        return round(total, 2)
    elif product == "coke":
        total = quantity * 1.40
        return round(total, 2)
    elif product == "snacks":
        total = quantity * 2.00
        return round(total, 2)

current_product = input()
current_quantity = float(input())

final_price = Total_price(current_product, current_quantity)

print(f"{final_price:.2f}")