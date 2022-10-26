package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.exceptions.TriangleException;
import ArchitecturePO.Lesson3.Shape.interFaceAction.ITriangleable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

public class Triangle extends Shape implements ITriangleable {
    private final int side1;
    private final int side2;
    private final int side3;

    public Triangle(int side1, int side2, int side3) {
        this.side1 = side1;
        this.side2 = side2;
        this.side3 = side3;
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
        return ITriangleable.super.IArea(side1, side2, side3);
    }
    @Override
    public int perimeter() {
        return ITriangleable.super.IPerimeter(side1, side2, side3);
    }
}