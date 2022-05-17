persons = int(input())
capacity = int(input())

left = persons % capacity
result = persons // capacity

if left > 0:
    result += 1

print(result)