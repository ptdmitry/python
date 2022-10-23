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


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass

    @abc.abstractmethod
    def perimeter(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

    def perimeter(self):
        return 2 * (self.length + self.width)


class Treangle(Shape):
    def __init__(self, height, footer, side_1, side_2):
        self.height = height
        self.footer = footer
        self.side_1 = side_1
        self.side_2 = side_2

    def area(self):
        return (self.height * self.footer) / 2

    def perimeter(self):
        return self.footer + self.side_1 + self.side_2


class Square(Shape):
    def __init__(self, length):
        self.length = length

    def area(self):
        return self.length**2

    def perimeter(self):
        return 4 * self.length


class Circle(Shape):
    def __init__(self, radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius**2

    def perimeter(self):
        return 3.14 * self.radius * 2


class ShapeFactory:
    def create_shape(self, name):
        if name == 'circle':
            radius = float(input('Введите радиус круга: '))
            if radius > 0:
                return Circle(radius)
        elif name == 'rectangle':
            length = int(input('Введите длину прямоугольника: '))
            width = int(input('Введите ширину прямоугольника: '))
            if length > 0 and width > 0:
                return Rectangle(length, width)
        elif name == 'square':
            length = int(input('Введите сторону квадрата: '))
            if length > 0:
                return Square(length)
        elif name == 'treangle':
            height = int(input('Введите высоту треугольника: '))
            footer = int(input('Введите основание треугольника: '))
            side_1 = int(input('Введите сторону треугольника: '))
            side_2 = int(input('Введите сторону треугольника: '))
            if height > 0 and footer > 0 and side_1 > 0 and side_2 > 0:
                return Treangle(height, footer, side_1, side_2)


def shapes_client():
    shape_arr = ['square', 'circle', 'rectangle', 'treangle']
    try:
        shape_factory = ShapeFactory()
        shape_name = input('Введите название фигуры (square, circle, rectangle или treangle: ').lower()
        if shape_name in shape_arr:
            shape = shape_factory.create_shape(shape_name)
            print(f'Площадь фигуры {shape_name}: {shape.area()}')
            print(f'Периметр (длина окружности) фигуры {shape_name}: {shape.perimeter()}')
        else:
            print('Ошибка! Нет такой фигуры')
    except AttributeError:
        print('Ошибка! Ввели отрицательное число или ноль')
    except ValueError:
        print('Ошибка! Ввели символ, не число')


shapes_client()
