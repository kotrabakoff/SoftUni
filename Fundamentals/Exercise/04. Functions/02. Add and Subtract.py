def sum_numbers(a, b):
    sum = a + b
    return sum

def subtract(current_sum, c):
    result = current_sum - c
    return result

first = int(input())
second = int(input())
third = int(input())

print(subtract(sum_numbers(first, second), third))