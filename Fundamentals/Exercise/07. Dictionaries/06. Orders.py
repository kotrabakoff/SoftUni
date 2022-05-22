initial = input()
storage = {}

while initial != "buy":
    initial_list = initial.split(" ")
    product = initial_list[0]
    price = float(initial_list[1])
    quantity = int(initial_list[2])
    if product in storage:
        new_quantity = storage[product][1] + quantity
        storage[product] = [price, new_quantity]
    else
        storage[product] = [price, quantity]

    initial = input()

for key in storage:
    final_quantity = storage[key][0] * storage[key][1]
    print(f"{key} -> {final_quantity:.2f}")