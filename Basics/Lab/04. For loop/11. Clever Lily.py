age = int(input())
washingMachine = float(input())
toyPrice = int(input())

sum = 0

for birthdayNumber in range(1, age+1):
    if birthdayNumber % 2 == 0:
        sum += birthdayNumber * 5
        sum -= 1
    else:
        sum += toyPrice

if sum >= washingMachine:
    print(f"Yes! {sum - washingMachine:.2f}")
else:
    print(f"No! {washingMachine - sum:.2f}")
