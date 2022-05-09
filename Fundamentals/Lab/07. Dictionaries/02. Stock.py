initial = input().split(" ")
products = {}

for i in range(0, len(initial), 2):
    key = initial[i]
    value = int(initial[i+1])
    products[key] = value

search = input().split(" ")

for search_item in search:
    if search_item in products.keys():
        print(f"We have {products[search_item]} of {search_item} left")
    else:
        print(f"Sorry, we don't have {search_item}")
