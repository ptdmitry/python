package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.exceptions.RectangleException;
import ArchitecturePO.Lesson3.Shape.interFaceAction.IPolygonable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

public class Rectangle extends Shape implements IPolygonable {
    private static int length;
    private static int width;

    public Rectangle(int length, int width) {
        Rectangle.length = length;
        Rectangle.width = width;
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
        return IPolygonable.super.IArea(length, width);
    }
    public static int perimeter() {
        return IPolygonable.IPerimeter(length, width);
    }
}