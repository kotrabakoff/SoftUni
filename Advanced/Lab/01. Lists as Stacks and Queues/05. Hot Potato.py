from collections import deque

sequence = deque(input().split())

tosses = int(input())
counter = 0
while len(sequence) > 1:
    counter += 1
    if counter == tosses:
        kid = sequence.popleft()
        print(f"Removed {kid}")
        counter = 0
    else:
        sequence.append(sequence.popleft())
    # print(f"Removed {sequence[-(counter - 1)]}")
    # del sequence[-(counter - 1)]


print(f"Last is {''.join(sequence)}")