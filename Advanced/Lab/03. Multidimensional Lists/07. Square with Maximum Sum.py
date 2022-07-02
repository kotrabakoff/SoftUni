n, m = [int(i) for i in input().split(", ")]

matrix = []

for i in range(n):
    current = [int(i) for i in input().split(", ")]
    matrix.append(current)

total = 0


for row in range(n-1):
    for column in range(m-1):
        current_square = [matrix[row][column],matrix[row][column+1],matrix[row+1][column],matrix[row+1][column+1]]
        if total < sum(current_square):
            total = sum(current_square)
            final_square = current_square

print(f"{final_square[0]} {final_square[1]}")
print(f"{final_square[2]} {final_square[3]}")
print(total)