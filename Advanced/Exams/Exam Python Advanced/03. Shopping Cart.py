def shopping_cart(*args):
    final = dict()
    for i in args:
        if i == "Stop":
            break
        meal = i[0]
        product = i[1]
        if meal in final:
            final[meal].append(product)
        else:
            final[meal] = []
            final[meal].append(product)
    last_string = str()
    for key in final:
        last_string += f"{key}\n"
        for k in final[key]:
            last_string += f" - {k}\n"
    return last_string


print(shopping_cart(
    ('Pizza', 'ham'),
    ('Soup', 'carrots'),
    ('Pizza', 'cheese'),
    ('Pizza', 'flour'),
    ('Dessert', 'milk'),
    ('Pizza', 'mushrooms'),
    ('Pizza', 'tomatoes'),
    'Stop',
))





