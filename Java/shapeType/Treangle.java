package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.Shape;

import java.util.Scanner;

public class Treangle extends Shape {
    Scanner scanner = new Scanner(System.in);
    int height = scanner.nextInt();
    int footer = scanner.nextInt();
    int side1 = scanner.nextInt();
    int side2 = scanner.nextInt();
    public int Area() {
        if (height <= 0 || footer <= 0 || side1 <= 0 || side2 <= 0) {
            throw new RuntimeException("Ошибка! Ввели отрицательное число или ноль");
        }
        System.out.println("Площадь треугольника:");
        return (height * footer) / 2;
    }
    public int Perimeter() {
        System.out.println("Периметр прямоугольника:");
        return side1 + side2 + footer;
    }
}