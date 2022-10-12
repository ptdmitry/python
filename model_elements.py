"""
На основе Диаграмы классов ModelElements, разработать классы:
Model Store, PoligonalModel (Texture, Poligon), Flash, Camera, Scene
"""


class Camera:
    def __init__(self, location, angle):
        self.Point3D = location
        self.Angle3D = angle

    def rotate(self):
        Angle3D()

    def move(self):
        Point3D()


class Flash:
    def __init__(self, location, angle, color, float):
        self.Point3D = location
        self.Angle3D = angle
        self.Color = color
        self.Power = float

    def rotate(self):
        Angle3D()

    def move(self):
        Point3D()


class Scene:
    def __init__(self, id: int, models, flashes):
        self.id = id
        self.PoligonalModel = models
        self.Flash = flashes

    def method_1(self, type_1):
        pass

    def method_2(self, type_1, type_2):
        pass


class PoligonalModel:
    def __init__(self, poligons, textures):
        self.Poligon = poligons
        self.Texture = textures


class Texture:
    pass


class Poligon:
    def __init__(self, points):
        self.Point3D = points


class Point3D:
    pass


class Angle3D:
    pass
