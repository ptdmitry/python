# Круг, Квадрат, Прямоугольник. Фабричный метод

import abc


class Shape(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def area(self):
        pass


class Rectangle(Shape):
    def __init__(self, length, width):
        self.height = length
        self.width = width

    def area(self):
        return self.height * self.width

    def perimeter(self):
        return 2 * (self.height + self.width)


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

    def circle_length(self):
        return 3.14 * self.radius * 2


class ShapeFactory:
    def create_shape(self, name):
        if name == 'circle':
            radius = input('Введите радиус круга: ')
            return Circle(float(radius))
        elif name == 'rectangle':
            length = input('Введите длину прямоугольника: ')
            width = input('Введите ширину прямоугольника: ')
            return Rectangle(int(length), int(width))
        elif name == 'square':
            length = input('Enter the width of the square: ')
            return Square(int(length))


def shapes_client():
    shape_factory = ShapeFactory()
    shape_name = input('Введите название фигуры: ')

    shape = shape_factory.create_shape(shape_name)

    if shape_name == 'circle':
        print(f'Площадь фигуры {shape_name}: {shape.area():.2f}')
        print(
            f'Длина окружности фигуры {shape_name}: {shape.circle_length():.2f}')
    else:
        print(f'Площадь фигуры {shape_name}: {shape.area()}')
        print(
            f'Периметр (длина окружности) фигуры {shape_name}: {shape.perimeter()}')


shapes_client()
