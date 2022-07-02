directions = {
    "up": lambda x, y: (x - 1, y),
    "down": lambda x, y: (x + 1, y),
    "left": lambda x, y: (x, y - 1),
    "right": lambda x, y: (x, y + 1)
}

size = int(input())

matrix = []

for i in range(size):
    current_row = [j for j in input().split()]
    matrix.append(current_row)
    for j in range(size):
        if current_row[j] == "B":
            bunny_row = i
            bunny_col = j

best_direction = ''
best_route = []
best_sum = float('-inf')

for direction in directions:
    current_sum = 0
    current_route = []
    current_place = []
    row, col = directions[direction](bunny_row, bunny_col)
    while 0 <= int(row) < size and 0 <= int(col) < size and matrix[row][col] != "X":
        current_sum += int(matrix[row][col])
        current_place = [row, col]
        current_route.append(current_place)
        if current_sum > best_sum:
            best_direction = direction
            best_route = current_route
            best_sum = current_sum
        row, col = directions[direction](row, col)

print(best_direction)
for i in best_route:
    print(i)
print(best_sum)