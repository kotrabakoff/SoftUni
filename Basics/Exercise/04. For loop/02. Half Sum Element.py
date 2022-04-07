import sys
n = int(input())

sum = 0
max = -sys.maxsize

for number in range(1, n+1):
    value = int(input())
    sum += value
    if value > max:
        max = value


if max == sum - max:
    print("Yes")
    print(f"Sum = {max}")
else:
    print("No")
    print(f"Diff = {abs(max - (sum - max))}")
