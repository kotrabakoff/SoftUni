def Groups(a):
    group = 10
    current_list = []
    for j in range(10, 110, 10):
        for i in a:
            if i <= j:
                current_list.append(i)
            else:
                continue
        if len(a) <= 0:
            break
        print(f"Group of {j}'s: {current_list}")
        a = [i for i in a if i not in current_list]
        current_list = []


initial = list(map(int, input().split(", ")))
Groups(initial)

