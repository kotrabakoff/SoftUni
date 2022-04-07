budget = int(input())
season = input()
fishermen = int(input())

if fishermen <= 6:
    if season == "Spring":
        price = 3000 * 0.9
    elif season == "Summer" or season == "Autumn":
        price = 4200 * 0.9
    else:
        price = 2600 * 0.9
elif 7 <= fishermen <= 11:
    if season == "Spring":
        price = 3000 * 0.85
    elif season == "Summer" or season == "Autumn":
        price = 4200 * 0.85
    else:
        price = 2600 * 0.85

else:
    if season == "Spring":
        price = 3000 * 0.75
    elif season == "Summer" or season == "Autumn":
        price = 4200 * 0.75
    else:
        price = 2600 * 0.75

if season == "Spring" or season == "Summer" or season == "Winter":
    if fishermen % 2 == 0:
        price -= price * 0.05

if budget >= price:
    print(f"Yes! You have {budget - price:.2f} leva left.")
else:
    print(f"Not enough money! You need {price - budget:.2f} leva.")
