from math import pow, floor

n = int(input())

for i in range(0, n+1, 2):
    print(floor(pow(2, i)))


