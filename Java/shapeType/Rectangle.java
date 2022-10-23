package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.Shape;

import java.util.Scanner;

public class Rectangle extends Shape {
    Scanner scanner = new Scanner(System.in);
    int length = scanner.nextInt();
    int width = scanner.nextInt();
    public int Area() {
        if (length <= 0 || width <= 0) {
            throw new RuntimeException("Ошибка! Ввели отрицательное число или ноль");
        }
        System.out.println("Площадь прямоугольника:");
        return length * width;
    }
    public int Perimeter() {
        System.out.println("Периметр прямоугольника:");
        return (length + width) * 2;
    }
}