/* Написать любом языке программирования, в которой идёт со следующими геометрическими фигурами:
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
 */

package ArchitecturePO.Lesson3.Shape;

import ArchitecturePO.Lesson3.Shape.shapeType.Circle;
import ArchitecturePO.Lesson3.Shape.shapeType.Rectangle;
import ArchitecturePO.Lesson3.Shape.shapeType.Square;
import ArchitecturePO.Lesson3.Shape.shapeType.Triangle;

import java.util.Objects;

public class ProgramShape {

    public static void main(String[] args) {

        Shape[] shapes = {new Square(4),
                new Rectangle(5, 10),
                new Triangle(3, 4, 5),
                new Circle(4)};

        for (Shape sh : shapes)
            if (Objects.equals(sh.name(), "Круг")) {
                System.out.println(sh.name() + ". Площадь = " + sh.area() + ". Длина окружности = " + sh.circleLength());
            } else {
                System.out.println(sh.name() + ". Площадь = " + sh.area() + ". Периметр = " + sh.perimeter());
            }
    }
}