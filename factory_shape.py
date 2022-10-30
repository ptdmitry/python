"""
Написать любом языке программирования, в которой идёт со следующими геометрическими фигурами:
1. Треугольник
2. Квадрат
3. Прямоугольник.
4. Круг

В программе имеется массив фигур, с которым можно сделать следующие операции:
1. Добавить новую фигуру
2. Посчитать периметр у всех фигур
3. Посчитать площадь у всех фигур

Для фигуры использовать базовый абстрактный класс фигуры, у которого есть методы
посчитать периметр и посчитать площадь фигуры. Массив фигур в программе должен быть
представлен как массив объектов этого базового класса. Массив фигур должен создаваться
и вся работа с ним идёт внутри main. При создании фигур необходимо осуществлять
проверку входных данных на возможность создания данной фигуры и в случае ошибки
выдавать соответствующие сообщения.
"""

import abc
from math import pi


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def name(self):
        pass

    @abc.abstractmethod
    def area(self):
        pass


class Polygon(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def perimeter(self):
        pass


class Circle(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def circle_length(self):
        pass


class Square(Shape, Polygon):
    def __init__(self, length):
        if length > 0:
            self.length = length

    def name(self):
        return 'Квадрат'

    def area(self):
        return self.length**2

    def perimeter(self):
        return 4 * self.length


class Rectangle(Shape, Polygon):
    def __init__(self, length, width):
        if length > 0 and width > 0:
            self.length = length
            self.width = width

    def name(self):
        return 'Прямоугольник'

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Triangle(Shape, Polygon):
    def __init__(self, side_1, side_2, side_3):
        if (side_1 + side_2) > side_3 and (side_2 + side_3) > side_1 and (side_1 + side_3) > side_2:
            self.side_1 = side_1
            self.side_2 = side_2
            self.side_3 = side_3

    def name(self):
        return 'Треугольник'

    def area(self):
        return self.perimeter() / 2

    def perimeter(self):
        return self.side_1 + self.side_2 + self.side_3


class CircleShape(Shape, Circle):
    def __init__(self, radius):
        if radius > 0:
            self.radius = radius

    def name(self):
        return 'Круг'

    def area(self):
        return pi * self.radius**2

    def circle_length(self):
        return pi * self.radius * 2


def create_shape():
    try:
        square = Square(4)
        rectangle = Rectangle(2, 6)
        triangle = Triangle(8, 3, 6)
        circle = CircleShape(4)

        shapes_list = [square, rectangle, triangle, circle]

        for shape in shapes_list:
            if shape is circle:
                print(f'{shape.name()}. Площадь: {shape.area():.1f}. Длина окружности: {shape.circle_length():.1f}')
            else:
                print(f'{shape.name()}. Площадь: {shape.area()}. Периметр: {shape.perimeter()}')
    except TypeError:
        print(f'Неверно заданы параметры фигуры. Символ вместо числа или ноль')
    except NameError:
        print(f'Неверно заданы параметры фигуры')
    except AttributeError:
        print(f'Фигуры "{shape.name()}" с такими параметрами не существует')


create_shape()
