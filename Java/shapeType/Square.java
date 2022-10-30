package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.exceptions.SquareException;
import ArchitecturePO.Lesson3.Shape.interFaceAction.IPolygonable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

public class Square extends Shape implements IPolygonable {
    private static int length;

    public Square(final int length) {
        Square.length = length;
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
        return IPolygonable.super.IArea(length);
    }
    public static int perimeter() {
        return IPolygonable.IPerimeter(length);
    }
}