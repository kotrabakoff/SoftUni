fruit = input()
day = input()
quantity = float(input())


if day == "Monday" or day == "Tuesday" or day == "Wednesday" or day == "Thursday" or day == "Friday":
    if fruit == "banana":
        price = 2.5
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "apple":
        price = 1.2
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "orange":
        price = 0.85
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "grapefruit":
        price = 1.45
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "kiwi":
        price = 2.70
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "pineapple":
        price = 5.5
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "grapes":
        price = 3.85
        final_price = quantity * price
        print(f"{final_price:.2f}")
    else:
        print("error")

elif day == "Saturday" or day == "Sunday":
    if fruit == "banana":
        price = 2.7
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "apple":
        price = 1.25
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "orange":
        price = 0.90
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "grapefruit":
        price = 1.60
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "kiwi":
        price = 3.00
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "pineapple":
        price = 5.6
        final_price = quantity * price
        print(f"{final_price:.2f}")
    elif fruit == "grapes":
        price = 4.2
        final_price = quantity * price
        print(f"{final_price:.2f}")
    else:
        print("error")
else:
    print("error")

