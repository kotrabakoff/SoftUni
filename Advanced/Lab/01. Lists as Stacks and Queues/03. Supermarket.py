from collections import deque

initial = input()

queue = deque()



while initial != "End":
    if initial == "Paid":
        for i in queue:
            print(i)
        # string = '\n'.join(queue)
        # print(f"{string}")
        queue = deque()
    else:
        queue.append(initial)
    initial = input()

counter = 0

for i in queue:
    counter += 1

print(f"{counter} people remaining.")
