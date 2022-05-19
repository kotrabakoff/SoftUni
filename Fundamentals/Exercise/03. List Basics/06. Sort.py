def Sort(a):
    result = sorted(a)
    return result

numbs_For_Sorting = list(map(int, input().split(" ")))

print(Sort(numbs_For_Sorting))