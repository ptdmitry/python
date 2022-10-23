package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.Shape;

import java.util.Scanner;

public class Circle extends Shape {

    Scanner scanner = new Scanner(System.in);
    int radius = scanner.nextInt();

    public int Area() {
        if (radius <= 0) {
            throw new RuntimeException("Ошибка! Ввели отрицательное число или ноль");
        }
        System.out.println("Площадь круга:");
        return (int)(3.14 * radius * radius);
    }
    public int Perimeter() {
        System.out.println("Длина окружности круга:");
        return (int) (3.14 * radius * 2);
    }
}