elements = int(input())

all_elements = []
unique_elements = {}

for i in range(elements):
    current_element = input().split()
    all_elements.extend(current_element)

unique_elements = set(all_elements)

for j in unique_elements:
    print(j)

