sequence = int(input())

all_names = set()

for i in range(sequence):
    name = input()
    all_names.add(name)

for j in all_names:
    print(f"{j}")
