money = input()
sum = 0.0

while money != "NoMoreMoney":
    number = float(money)
    if number < 0:
        print("Invalid operation!")
        break
    sum += number
    print(f"Increase: {number:.2f}")
    money = input()

print(f"Total: {sum:.2f}")
