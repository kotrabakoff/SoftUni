days = int(input())
place = input()
feedback = input()

days -= 1

if place == "room for one person":
    price = 18 * days

elif place == "apartment":
    if days < 10:
        price = (25 * days) * 0.7
    elif 10 <= days <= 15:
        price = (25 * days) * 0.65
    else:
        price = (25 * days) * 0.5

elif place == "president apartment":
    if days < 10:
        price = (35 * days) * 0.9
    elif 10 <= days <= 15:
        price = (35 * days) * 0.85
    else:
        price = (35 * days) * 0.80

if feedback == "positive":
    final_price = price + price * 0.25
else:
    final_price = price - price * 0.1

print(f"{final_price:.2f}")