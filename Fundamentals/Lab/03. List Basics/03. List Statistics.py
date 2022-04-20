n = int(input())
positive = []
negative = []

for i in range(0, n):
    number = int(input())
    if number >= 0:
        positive.append(number)
    else:
        negative.append(number)

print(positive)
print(negative)


print(f"Count of positives: {len(positive)}")
print(f"Sum of negatives: {sum(negative)}")