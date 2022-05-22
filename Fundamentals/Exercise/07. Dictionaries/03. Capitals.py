countries = input().split(", ")
cities = input().split(", ")

altogether = zip(countries, cities)
altogether_list = list(altogether)

d = {key: str(value) for key, value in altogether_list}

for key in d:
    print(f"{key} -> {d[key]}")
