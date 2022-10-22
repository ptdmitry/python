// Круг, Квадрат, Прямоугольник. Фабричный метод

package ArchitecturePO.Lesson3.Shape;

import ArchitecturePO.Lesson3.Shape.interFaceAction.ICircleable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.ISquareable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;
import ArchitecturePO.Lesson3.Shape.shapeType.Circle;
import ArchitecturePO.Lesson3.Shape.shapeType.Rectangle;
import ArchitecturePO.Lesson3.Shape.shapeType.Square;

import java.util.Objects;
import java.util.Scanner;

public class ProgramShape {
    public static void main(String[] args) {
        System.out.println("Введите название фигуры (square, rectangle или circle): ");
        Scanner scanner = new Scanner(System.in);
        String nameShape = scanner.nextLine();
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
        } else {
            System.err.println("Неверно введена фигура");
        }
    }

    public static void printShapeInfo(Shape shape) {
        System.out.println(shape.Area());
        if (shape instanceof ICircleable) {
            System.out.println(((ICircleable) shape).CircleLength());
        } else if (shape instanceof ISquareable) {
            System.out.println(((ISquareable) shape).Perimeter());
        }
    }
}