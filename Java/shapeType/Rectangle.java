package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.interFaceAction.ISquareable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

import java.util.Scanner;

public class Rectangle extends Shape implements ISquareable {
    Scanner scanner = new Scanner(System.in);
    int length = scanner.nextInt();
    int width = scanner.nextInt();
    public int Area() {
        System.out.println("Площадь прямоугольника:");
        return length * width;
    }
    public int Perimeter() {
        System.out.println("Периметр прямоугольника:");
        return (length + width) * 2;
    }
}