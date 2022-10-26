package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.exceptions.SquareException;
import ArchitecturePO.Lesson3.Shape.interFaceAction.IRectangleable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

public class Square extends Shape implements IRectangleable {
    private final int length;

    public Square(final int length) {
        this.length = length;
        if (length <= 0) {
            throw new SquareException();
        }
    }
    @Override
    public String name() {
        return "Квадрат";
    }
    @Override
    public int area() {
        return IRectangleable.super.IArea(length);
    }
    @Override
    public int perimeter() {
        return IRectangleable.super.IPerimeter(length);
    }
}