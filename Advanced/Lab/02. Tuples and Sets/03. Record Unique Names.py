repeats = int(input())

all = set()

for i in range(repeats):
    name = input()
    all.add(name)

for j in all:
    print(j)