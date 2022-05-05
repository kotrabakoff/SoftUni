def Sorter(a):
    sorted_list = sorted(a, key = lambda x: (-len(x), x))
    return sorted_list

initial = input().split(", ")

print(Sorter(initial))