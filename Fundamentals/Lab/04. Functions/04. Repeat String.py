def Repeater(string, n):
    result = string * n
    return result

current_string = input()
current_n = int(input())

print(Repeater(current_string, current_n))