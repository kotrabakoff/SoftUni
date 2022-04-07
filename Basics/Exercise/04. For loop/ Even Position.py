import sys
n = int(input())

max_even = -sys.maxsize
min_even = sys.maxsize
max_odd = -sys.maxsize
min_odd = sys.maxsize
sum_even = 0
sum_odd = 0

for number in range(1, n+1):
    value = float(input())
    if number % 2 == 0:
        sum_even += value
        if value > max_even:
            max_even = value
        if value < min_even:
            min_even = value
    else:
        sum_odd += value
        if value > max_odd:
            max_odd = value
        if value < min_odd:
            min_odd = value

print(f"OddSum={sum_odd:.2f},")

if min_odd == sys.maxsize:
    print("OddMin=No,")
else:
    print(f"OddMin={min_odd:.2f},")

if max_odd == -sys.maxsize:
    print("OddMax=No,")
else:
    print(f"OddMax={max_odd:.2f},")

print(f"EvenSum={sum_even:.2f},")

if min_even == sys.maxsize:
    print("EvenMin=No,")
else:
    print(f"EvenMin={min_even:.2f},")

if max_even == -sys.maxsize:
    print("EvenMax=No")
else:
    print(f"EvenMax={max_even:.2f}")
