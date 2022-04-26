def Smallest_number(a, b, c):
    if a < b and a < c:
        return a
    elif b < a and b < c:
        return b
    elif c < a and c < b:
        return c
n
first = int(input())
second = int(input())
third = int(input())

print(Smallest_number(first, second, third))