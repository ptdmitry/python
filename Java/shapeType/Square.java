package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.interFaceAction.ISquareable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

import java.util.Scanner;

public class Square extends Shape implements ISquareable {
    Scanner scanner = new Scanner(System.in);
    int length = scanner.nextInt();
    public int Area() {
        System.out.println("Площадь квадрата:");
            return length * length;
        }
    public int Perimeter() {
        System.out.println("Периметр квадрата:");
        return length * 4;
    }
}