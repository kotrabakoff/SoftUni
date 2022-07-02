def sorting_cheeses(**kwargs):
    final = []
    quantity_list = []
    sorted_dict = sorted(kwargs.items(), key=lambda x: (-len(x[1]), x[0]))
    for key,value in sorted_dict:
        final.append(key)
        quantity_list = sorted(value, reverse=True)
        final += quantity_list
    return '\n'.join([str(x)for x in final])

print(
    sorting_cheeses(
        Parmesan=[102, 120, 135],
        Camembert=[100, 100, 105, 500, 430],
        Mozzarella=[50, 125],
    )
)

