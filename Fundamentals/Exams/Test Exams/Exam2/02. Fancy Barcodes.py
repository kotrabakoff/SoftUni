import re

counts = int(input())
pattern = r"(@\#+)([A-Z])([A-Za-z0-9]{4,})([A-Z])(@\#+)"

for i in range(0, counts):
    text = input()
    match = re.match(pattern, text)
    if match is not None:
        final = []
        stripped_match = match[3]
        find = re.findall(r"[0-9]", stripped_match)
        if len(find) > 0:
            print(f"Product group: {''.join(find)}")
        else:
            print("Product group: 00")
    else:
        print("Invalid barcode")