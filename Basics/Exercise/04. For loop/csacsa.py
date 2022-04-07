import sys
numbers = float(input())

oddMin = sys.maxsize
oddMax = -sys.maxsize
oddSum = 0
evenMin = sys.maxsize
evenMax = -sys.maxsize
evenSum = 0

for number in (1, numbers+1):
    value = float(input())
    if number % 2 == 0:
        evenSum += value
        if evenMax < value
            value