def Evens(a):
    string = filter(lambda i: i % 2 == 0, a)
    evens = list(string)
    return evens


numb_sequence = list(map(int, input().split(" ")))

print(Evens(numb_sequence))