from collections import deque

sequence_eggs_size = deque([int(x) for x in input().split(", ")])
paper_sizes = [int(x) for x in input().split(", ")]

boxes_counter = 0

for i in range(len(sequence_eggs_size)):
    if sequence_eggs_size and paper_sizes:
        current_egg = sequence_eggs_size[0]
        current_paper = paper_sizes[-1]
        if current_egg <= 0:
            sequence_eggs_size.popleft()
            continue
        if current_egg == 13:
            temp = paper_sizes[0]
            paper_sizes[0] = paper_sizes[len(paper_sizes) - 1]
            paper_sizes[len(paper_sizes) - 1] = temp
            sequence_eggs_size.popleft()
            continue
        sum = current_egg + current_paper
        if sum <= 50:
            sequence_eggs_size.popleft()
            paper_sizes.pop()
            boxes_counter += 1
        elif sum > 50:
            sequence_eggs_size.popleft()
            paper_sizes.pop()
    else:
        break


if boxes_counter > 0:
    print(f"Great! You filled {boxes_counter} boxes.")
else:
    print(f"Sorry! You couldn't fill any boxes!")

if sequence_eggs_size:
    print(f"Eggs left: {', '.join([str(x) for x in sequence_eggs_size])}")
if paper_sizes:
    print(f"Pieces of paper left: {', '.join([str(x) for x in paper_sizes])}")