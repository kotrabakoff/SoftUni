month = input()
nights = int(input())

studio = 76
apartment = 77

if month == "May" or month == "October":
    studio = 50
    apartment = 65
    if nights > 14:
        studio *= 0.7
        apartment *= 0.9
    elif 7 < nights:
        studio *= 0.95

elif month == "June" or month == "September":
    studio = 75.2
    apartment = 68.7
    if nights > 14:
        studio *= 0.8
        apartment *= 0.9
else:
    if nights > 14:
        apartment *= 0.9


print(f"Apartment: {apartment * nights:.2f} lv.")
print(f"Studio: {studio * nights:.2f} lv.")