n, m = [int(i) for i in input().split(" ")]

current = []
matrix = []

start = 97
middle = 96

for row in range(n):
    middle = start
    for column in range(m):
        pali = chr(start) + chr(middle) + chr(start)
        current.append(pali)
        middle += 1
    matrix.append(current)
    current = []
    start += 1

for i in matrix:
    print(f"{' '.join(i)}")