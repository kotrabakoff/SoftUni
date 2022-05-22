contact = input()
all_contact = {}


while "-" in contact:
    separated = contact.split("-")
    key = separated[0]
    value = separated[1]
    if key not in all_contact:
        all_contact[key] = value
    else:
        all_contact[key] += value
    contact = input()

for i in range(0, int(contact)):
    search_name = input()

    if search_name in all_contact.keys():
        print(f"{search_name} -> {all_contact[search_name]}")
    else:
        print(f"Contact {search_name} does not exist.")