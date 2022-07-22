class Glass:
    capacity = 250
    def __init__(self):
        self.content = 0

    def fill(self, ml):
        left = self.space_left()
        if left < ml:
            return f"Cannot add {ml} ml"

        self.content += ml
        return f"Glass filled with {ml} ml"


    def empty(self):
        self.content = 0
        return "Glass is now empty"

    def info(self):
        left = self.space_left()
        return f"{left} ml left"

    def space_left(self):
        left = self.capacity - self.content
        return left

glass = Glass()
print(glass.fill(100))
print(glass.fill(200))
print(glass.empty())
print(glass.fill(200))
print(glass.info())
