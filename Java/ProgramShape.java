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
import ArchitecturePO.Lesson3.Shape.shapeType.Treangle;

import java.util.Arrays;
import java.util.InputMismatchException;
import java.util.Objects;
import java.util.Scanner;

public class ProgramShape {
    public static void main(String[] args) {
        String[] shapes = new String[]{"square", "rectangle", "circle", "treangle"};

        System.out.println("Введите название фигуры (square, rectangle, treangle или circle): ");
        Scanner scanner = new Scanner(System.in);
        String nameShape = scanner.nextLine();
        boolean test = Arrays.asList(shapes).contains(nameShape);
        if (test) {
            try {
                if (Objects.equals(nameShape, "square")) {
                    System.out.println("Введите сторону квадрата: ");
                    Square square = new Square();
                    printShapeInfo(square);
                } else if (Objects.equals(nameShape, "rectangle")) {
                    System.out.println("\nВведите длину и ширину прямоугольника: ");
                    Rectangle rectangle = new Rectangle();
                    printShapeInfo(rectangle);
                } else if (Objects.equals(nameShape, "circle")) {
                    System.out.println("\nВведите радиус круга: ");
                    Circle circle = new Circle();
                    printShapeInfo(circle);
                } else if (Objects.equals(nameShape, "treangle")) {
                    System.out.println("\nВведите высоту, основание и стороны треугольника: ");
                    Treangle treangle = new Treangle();
                    printShapeInfo(treangle);
                }
            } catch (InputMismatchException e) {
                System.err.println("Ошибка! Ввели символ, не число");
            }
        } else {
            System.err.println("Ошибка! Нет такой фигуры");
        }
    }

    public static void printShapeInfo(Shape shape) {
        System.out.println(shape.Area());
        System.out.println(shape.Perimeter());
    }
}