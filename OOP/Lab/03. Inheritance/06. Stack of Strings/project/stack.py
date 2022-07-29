class Stack:
    def __init__(self):
        self.data = []

    def validate_if_string(self, value):
        if not isinstance(value, str):
            raise TypeError('Only strings can be appended to class Stack')

    def push(self, element):
        self.validate_if_string(element)
        self.data.append(element)

    def pop(self):
        return self.data.pop()

    def top(self):
        return self.data[-1]

    def is_empty(self):
        return len(self.data) == 0

    def __str__(self):
        return f"[{', '.join(reversed(self.data))}]"

