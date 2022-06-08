from collections import deque

quantity = int(input())

orders = input().split()

orders = deque([int(x) for x in orders])

print(f"{max(orders)}")

for i in range(len(orders)):
    current = int(orders[0])
    if current <= quantity:
        orders.popleft()
        quantity -= current
    else:
        break

if len(orders) == 0:
    print("Orders complete")
else:
    orders = [str(x) for x in orders]
    print(f"Orders left: {' '.join(orders)}")