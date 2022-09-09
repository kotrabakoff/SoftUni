from project.animal import Animal

class Tiger(Animal):
    DEFAULT = 45

    def __init__(self, name, gender, age):
        super().__init__(name, gender, age, self.DEFAULT)


