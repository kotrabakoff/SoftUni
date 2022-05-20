def Substring(a, b):
    final_list = []
    for i in a:
        for j in b:
            if i in j:
                final_list.append(i)
                break
    return final_list


first = input().split(", ")
second = input().split(", ")

print(Substring(first, second))