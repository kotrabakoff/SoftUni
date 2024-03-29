class Cup():
    def __init__(self, size, quantity):
        self.size = size
        self.quantity = quantity
    def fill(self, milliliters):
        left = self.size - self.quantity
        if left >= milliliters:
            self.quantity += milliliters

    def status(self):
        left = self.size - self.quantity
        return left

cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())
