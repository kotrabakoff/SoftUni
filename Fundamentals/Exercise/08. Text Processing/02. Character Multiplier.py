def sum_fun(a, b):
    total_sum = 0

    for i in range(len(a)):
        if i < len(b):
            total_sum += ord(a[i]) * ord(b[i])
        else:
            total_sum += ord(a[i])
    return total_sum

def char_multiplier(a, b):
    result = 0
    if len(a) > len(b):
        result = sum_fun(a, b)
    else:
        result = sum_fun(b, a)
    print(result)

data = input().split(' ')
char_multiplier(data[0], data[1])

