times = int(input())

parking_lot = set()

for i in range(times):
    occurence = input().split(", ")
    command = occurence[0]
    plate = occurence[1]
    if command == "IN":
        parking_lot.add(plate)
    elif command == "OUT":
        parking_lot.remove(plate)

if len(parking_lot) <= 0:
    print("Parking Lot is Empty")
else:
    for car in parking_lot:
        print(car)

