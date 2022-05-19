start = int(input())
stop = int(input())

for i in range(start, stop + 1):
    char = chr(i)
    print(f"{char}", end= " ")
