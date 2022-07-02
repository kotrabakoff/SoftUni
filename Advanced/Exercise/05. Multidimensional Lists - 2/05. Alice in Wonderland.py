size = int(input())

matrix = []

for i in range(size):
    current_row = [j for j in input().split()]
    for j in range(size):
        if current_row[j] == "A":
            alice_row = i
            alice_col = j
    matrix.append(current_row)

directions = {
    "up": lambda x, y: (x-1, y),
    "down": lambda x, y: (x+1, y),
    "left": lambda x, y: (x, y-1),
    "right": lambda x, y: (x, y+1)
}

teabags = 0

row = alice_row
col = alice_col

while teabags < 10:
    direction = input()
    matrix[row].pop(col)
    matrix[row].insert(col, "*")
    row, col = directions[direction](row, col)
    if 0 <= row < size and 0 <= col < size:
        current_pos = matrix[row][col]
        if current_pos != "." and current_pos != "*":
            if current_pos != "R":
                teabags += int(current_pos)
                matrix[row].pop(col)
                matrix[row].insert(col, "*")
            else:
                matrix[row].pop(col)
                matrix[row].insert(col, "*")
                print("Alice didn't make it to the tea party.")
                break
        else:
            matrix[row].pop(col)
            matrix[row].insert(col, "*")
    else:
        print("Alice didn't make it to the tea party.")
        break


if teabags >= 10:
    print("She did it! She went to the party.")

for k in matrix:
    print(*k, end='\n')