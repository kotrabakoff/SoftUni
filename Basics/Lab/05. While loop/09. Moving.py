width = int(input())
length = int(input())
height = int(input())

cartons_input = input()
sum = 0
space = True
volume = width * length * height

while cartons_input != "Done":
    cartons = int(cartons_input)
    sum += cartons
    if sum > volume:
        space = False
        break
    cartons_input = input()

if space == True:
    print(f"{volume - sum} Cubic meters left.")
else:
    print(f"No more free space! You need {abs(sum - volume)} Cubic meters more.")
