from math import floor

proc_number = int(input())
staff_number = int(input())
working_days = int(input())

processors_availability = (working_days * 8 * staff_number) / 3

price = floor(processors_availability) * 110.1

losses = (proc_number * 110.1) - price

profit = (floor(processors_availability) - proc_number) * 110.1

if processors_availability >= proc_number:
    print(f"Profit: -> {profit:.2f} BGN")
else:
    print(f"Losses: -> {abs(losses):.2f} BGN")

