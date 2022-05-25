import re

def furniture_info():
    pattern = ''
    total = 0
    product_list = []
    while True:
        text = input()
        if text == "Purchase":
            break

        matches = re.match(r">>([a-zA-Z]+)<<(\d+|\d+\.\d+)!(\d+)", text)

        if matches is not None:
            product = matches[1]
            price = float(matches[2])
            quantity = float(matches[3])
            total += price * quantity
            product_list.append(product)

    print("Bought furniture:")
    if total > 0:
        string = "\n".join(product_list)
        print(f"{string}")
    print(f"Total money spend: {total:.2f}")


furniture_info()

# regex2 = re.findall(r"(?<=>)\d+[|][a-z]+[|][A-Z]+[|](\W+|\D+)(?=<)", text)
# print("|".join(regex))