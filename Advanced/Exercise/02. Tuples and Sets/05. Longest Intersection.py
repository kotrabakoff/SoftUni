sequence = int(input())
final_intersection = []

for i in range(sequence):
    ranges = input().split("-")
    range_1 = ranges[0].split(",")
    range_1 = [int(a) for a in range_1]
    range_1 = list(range(range_1[0],range_1[1]+1))
    range_2 = ranges[1].split(",")
    range_2 = [int(b) for b in range_2]
    range_2 = list(range(range_2[0],range_2[1]+1))
    current_intersection = list(set(range_1).intersection(range_2))
    if len(current_intersection) > len(final_intersection):
        final_intersection = current_intersection

print(f"Longest intersection is {final_intersection} with length {len(final_intersection)}")