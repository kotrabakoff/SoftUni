def get_info(**kwargs):
    name, town, age = tuple(kwargs.values())
    return f"This is {name} from {town} and he is {age} years old"

print(get_info(**{"name": "George", "town": "Sofia", "age": 20}))