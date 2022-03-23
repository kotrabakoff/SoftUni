N = int(input())
M = int(input())
S = int(input())

for address in range(M, N, -1):
    if address % 3 == 0:
        if address % 2 == 0:
            if address == S:
                break
            else:
                print(address, end=" ")

