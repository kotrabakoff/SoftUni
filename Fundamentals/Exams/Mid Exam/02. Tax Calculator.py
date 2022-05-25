initial = list(input().split(">>"))
total = 0

for i in initial:
    current_tax = 0
    i = list(i.split(" "))
    car_type = i[0]
    taxation_years = float(i[1])
    kilometers_traveled = float(i[2])
    if car_type == "family":
        current_tax += 50
        current_tax -= 5 * taxation_years
        current_tax += 12 * (kilometers_traveled // 3000)
        total += current_tax
        print(f"A {car_type} car will pay {current_tax:.2f} euros in taxes.")
    elif car_type == "heavyDuty":
        current_tax += 80
        current_tax -= 8 * taxation_years
        current_tax += 14 * (kilometers_traveled // 9000)
        total += current_tax
        print(f"A {car_type} car will pay {current_tax:.2f} euros in taxes.")
    elif car_type == "sports":
        current_tax += 100
        current_tax -= 9 * taxation_years
        current_tax += 18 * (kilometers_traveled // 2000)
        total += current_tax
        print(f"A {car_type} car will pay {current_tax:.2f} euros in taxes.")
    else:
        print("Invalid car type.")



print(f"The National Revenue Agency will collect {total:.2f} euros in taxes.")