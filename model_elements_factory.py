# Задание. Реализовать пример паттерна фабрики на примере диаграммы из предыдущего занятия для классов Flash и Camera

class Flash:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()
        self.color = Color()
        self.power = Float()

    def rotate(self, Angle_3D):
        pass

    def move(self, Point_3D):
        pass


class Camera:
    def __init__(self):
        self.location = Point3D()
        self.angle = Angle3D()

    def rotate(self, Angle_3D):
        pass

    def move(self, Point_3D):
        pass


class Point3D:
    pass


class Angle3D:
    pass


class Color:
    pass


class Float:
    pass


class ModelElementsFactory:
    def create_element(self, element):
        if element == 'Flash':
            return Flash()
        if element == 'Camera':
            return Camera()


def call_factory():
    flash_obj = ModelElementsFactory().create_element('Flash')
    print(f'The object is: {flash_obj}')
    print(f'The type of object created: {type(flash_obj)}\n')

    camera_obj = ModelElementsFactory().create_element('Camera')
    print(f'The object is: {camera_obj}')
    print(f'The type of object created: {type(camera_obj)}\n')


call_factory()
