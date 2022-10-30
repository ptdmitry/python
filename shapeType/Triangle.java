package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.exceptions.TriangleException;
import ArchitecturePO.Lesson3.Shape.interFaceAction.IPolygonable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

public class Triangle extends Shape implements IPolygonable {
    private static int side1;
    private static int side2;
    private static int side3;

    public Triangle(int side1, int side2, int side3) {
        Triangle.side1 = side1;
        Triangle.side2 = side2;
        Triangle.side3 = side3;
        if ((side1 + side2) <= side3 || (side2 + side3) <= side1 || (side1 + side3) <= side2) {
            throw new TriangleException();
        }
    }
    @Override
    public String name() {
        return "Треугольник";
    }
    @Override
    public int area() {
        return IPolygonable.super.IArea(side1, side2, side3);
    }
    public static int perimeter() {
        return IPolygonable.IPerimeter(side1, side2, side3);
    }
}