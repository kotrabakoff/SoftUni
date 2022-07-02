n, m = [int(i) for i in input().split(", ")]

matrix = []

for _ in range(n):
    current = [int(j) for j in input().split(" ")]
    matrix.append(current)

for k in range(m):
    current_column = [row[k] for row in matrix]
    print(sum(current_column))