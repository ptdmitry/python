package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.exceptions.RectangleException;
import ArchitecturePO.Lesson3.Shape.interFaceAction.IRectangleable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

public class Rectangle extends Shape implements IRectangleable {
    private final int length;
    private final int width;

    public Rectangle(int length, int width) {
        this.length = length;
        this.width = width;
        if (length <= 0 || width <= 0) {
            throw new RectangleException();
        }
    }
    @Override
    public String name() {
        return "Прямоугольник";
    }
    @Override
    public int area() {
        return IRectangleable.super.IArea(length, width);
    }
    @Override
    public int perimeter() {
        return IRectangleable.super.IPerimeter(length, width);
    }
}