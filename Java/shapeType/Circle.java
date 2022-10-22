package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.interFaceAction.ICircleable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

import java.util.Scanner;

public class Circle extends Shape implements ICircleable {
    Scanner scanner = new Scanner(System.in);
    int radius = scanner.nextInt();
    public int Area() {
        System.out.println("Площадь круга:");
        return (int)(3.14 * radius * radius);
    }
    public double CircleLength() {
        System.out.println("Длина окружности круга:");
        return 3.14 * radius * 2;
    }
}