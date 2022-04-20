n = int(input())
sum = 0

for i in range(0, n):
    litters = int(input())
    sum += litters
    if sum >= 255:
        print("Insufficient capacity!")
        sum -= litters
        continue



print(sum)