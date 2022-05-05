def Rounder(list):
    new_list = []
    for i in list:
        decimal = float(i)
        num = round(decimal)
        new_list.append(num)
    return new_list

current_list = input().split()

print(Rounder(current_list))