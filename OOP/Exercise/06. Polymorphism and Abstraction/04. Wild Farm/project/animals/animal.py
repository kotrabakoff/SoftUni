from abc import ABC, abstractmethod

from project.food import Food


class Animal(ABC):
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.food_eaten = 0

    @property
    @abstractmethod
    def allowed_foods(self):
        pass

    @property
    @abstractmethod
    def weight_incremental(self):
        pass

    @abstractmethod
    def make_sound(self):
        pass

    # @abc.abstractmethod
    # def __repr__(self):
    #     pass

    def feed(self, food: Food):
        food_name = food.__class__.__name__
        if food_name not in self.allowed_foods:
            return f"{self.__class__.__name__} does not eat {food.__class__.__name__}!"
        self.food_eaten += food.quantity
        self.weight += self.weight_incremental * food.quantity


class Bird(Animal):
    def __init__(self, name, weight, wing_size: float):
        super().__init__(name, weight)
        self.wing_size = wing_size


    def __repr__(self):
        return f"{self.__class__.__name__} [{self.name}, {self.wing_size}, {self.weight}, {self.food_eaten}]"



class Mammal(Animal):
    def __init__(self, name, weight, living_region: str):
        super().__init__(name, weight)
        self.living_region = living_region


