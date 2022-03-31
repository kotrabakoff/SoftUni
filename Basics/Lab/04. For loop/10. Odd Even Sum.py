n = int(input())

even = 0
odd = 0

for number in range(1, n+1):
    value = int(input())
    if number % 2 == 0:
        even += value
    else:
        odd +=value

if even == odd:
    print("Yes")
    print(f"Sum = {even}")
else:
    print("No")
    print(f"Diff = {abs(even - odd)}")
