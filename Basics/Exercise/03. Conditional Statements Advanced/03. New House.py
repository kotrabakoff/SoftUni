flowers = input()
numberFlowers = int(input())
budget = int(input())

price = 0

if flowers == "Roses":
    if numberFlowers > 80:
        price = (numberFlowers * 5) * 0.9
    else:
        price = numberFlowers * 5

elif flowers == "Dahlias":
    if numberFlowers > 90:
        price = (numberFlowers * 3.8) * 0.85
    else:
        price = numberFlowers * 3.8

elif flowers == "Tulips":
    if numberFlowers > 80:
        price = (numberFlowers * 2.8) * 0.85
    else:
        price = numberFlowers * 2.8

elif flowers == "Narcissus":
    if numberFlowers < 120:
        price = (numberFlowers * 3) + (numberFlowers * 3) * 0.15
    else:
        price = numberFlowers * 3

else:
    if numberFlowers < 80:
        price = (numberFlowers * 2.5) + (numberFlowers * 2.5) * 0.2
    else:
        price = numberFlowers * 2.5

if price <= budget:
    print(f"Hey, you have a great garden with {numberFlowers} {flowers} and {budget - price:.2f} leva left.")
else:
    print(f"Not enough money, you need {price - budget:.2f} leva more.")
