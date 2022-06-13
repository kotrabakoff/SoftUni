x_y = [int(i) for i in input().split(" ")]

biggest = max(x_y)
smallest = min(x_y)

rows, columns = x_y

matrix = []

for _ in range(rows):
    current = [i for i in input().split(" ")]
    matrix.append(current)

command = input()

while command != "END":
    command = command.split(" ")
    length = len(command)
    if command[0] != "swap" or length != 5:
        print("Invalid input!")
        command = input()
        continue
    a = int(command[1])
    b = int(command[2])
    c = int(command[3])
    d = int(command[4])
    if a > rows or b > columns or c > rows or d > columns or a < 0 or b < 0 or c < 0 or d < 0:
        print("Invalid input!")
        command = input()
        continue

    matrix[a][b], matrix[c][d] = matrix[c][d], matrix[a][b]
    for i in matrix:
        print(f"{' '.join([str(j) for j in i])}")
    command = input()