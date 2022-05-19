string_input = list(map(int, input().split()))
count = int(input())

for i in range(0, count):
    remove_number = min(string_input)
    string_input.remove(remove_number)


print(', '.join(map(str, string_input)))