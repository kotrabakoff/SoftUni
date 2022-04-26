def ASCII_inbetween(a, b):
    repeats = b - a
    start = a
    list = []
    for i in range(1, repeats):
        start += 1
        char = chr(start)
        list.append(char)
    string = " ".join(list)
    return string

first = ord(input())
second = ord(input())

print(ASCII_inbetween(first, second))



