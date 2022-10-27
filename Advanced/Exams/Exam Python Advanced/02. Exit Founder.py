order = input().split(", ")

rows = 6
matrix = []

Tom = True
Jerry = True

for i in range(rows):
    line_input = [j for j in input().split()]
    matrix.append(line_input)

counter = 0

skip_move = []

while Tom and Jerry:
    coordinates = input()
    counter += 1
    row = int(coordinates[1])
    column = int(coordinates[4])
    place = matrix[row][column]
    if counter % 2 == 1:
        current = order[0]
    else:
        current = order[1]
    if place == "W":
        skip_move.append(counter + 2)
        print(f"{current} hits a wall and needs to rest.")
    if counter in skip_move:
        continue
    if place == "E":
        print(f"{current} found the Exit and wins the game!")
        break
    elif place == "T":
        order.remove(current)
        print(f"{current} is out of the game! The winner is {''.join(order)}." )
        break

























