from abc import ABC, abstractmethod


class Horse(ABC):

    @abstractmethod
    def __init__(self, name, speed):
        self.name = name
        self.speed = speed
        self.is_taken = False

    @abstractmethod
    def train(self):
        pass

