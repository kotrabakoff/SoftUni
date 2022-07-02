rows = int(input())

matrix = []

for _ in range(rows):
    current = [int(i) for i in input().split(" ")]
    matrix.append(current)

index = 0
diagonal = 0

for j in matrix:
    diagonal += j[index]
    index += 1

print(diagonal)