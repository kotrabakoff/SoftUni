import abc
import math


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def calculate_area(self):
        pass

    @abc.abstractmethod
    def calculate_perimeter(self):
        pass


class Circle(Shape):
    def __init__(self, r):
        self.__r = r
        self.__pi = math.pi

    def calculate_area(self):
        return self.__r**2 * self.__pi

    def calculate_perimeter(self):
        return 2*self.__pi*self.__r


class Rectangle(Shape):
    def __init__(self, height, width):
        self.__height = height
        self.__width = width

    def calculate_area(self):
        return self.__height * self.__width

    def calculate_perimeter(self):
        return 2 * self.__height + 2 * self.__width

rectangle = Rectangle(10, 20)
print(rectangle.calculate_area())
print(rectangle.calculate_perimeter())

