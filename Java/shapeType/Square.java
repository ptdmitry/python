package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.Shape;

import java.util.Scanner;

public class Square extends Shape {
    Scanner scanner = new Scanner(System.in);
    int length = scanner.nextInt();
    public int Area() {
        if (length <= 0) {
            throw new RuntimeException("Ошибка! Ввели отрицательное число или ноль");
        }
        System.out.println("Площадь квадрата:");
            return length * length;
        }
    public int Perimeter() {
        System.out.println("Периметр квадрата:");
        return length * 4;
    }
}