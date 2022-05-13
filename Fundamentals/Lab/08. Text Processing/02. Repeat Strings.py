initial = input().split()
final = ""

for i in initial:
    final += i * len(i)

print(final)