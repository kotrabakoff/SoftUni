n, m = [int(i) for i in input().split(" ")]

matrix = []

for _ in range(n):
    current = [int(i) for i in input().split(" ")]
    matrix.append(current)

current_largest = []

for row in range(n - 2):
    for column in range(m - 2):
        current_submatrix = [matrix[row][column], matrix[row][column+1], matrix[row][column + 2], matrix[row+1][column], matrix[row+1][column+1], matrix[row+1][column + 2],matrix[row+2][column], matrix[row+2][column+1], matrix[row+2][column + 2]]
        if sum(current_submatrix) > sum(current_largest):
            current_largest = current_submatrix


print(f"Sum = {sum(current_largest)}")
print(current_largest[0], current_largest[1], current_largest[2])
print(current_largest[3], current_largest[4], current_largest[5])
print(current_largest[6], current_largest[7], current_largest[8])
