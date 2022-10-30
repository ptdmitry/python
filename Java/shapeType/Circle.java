package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.exceptions.CircleException;
import ArchitecturePO.Lesson3.Shape.interFaceAction.ICircleable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

public class Circle extends Shape implements ICircleable {
    private static int radius;

    public Circle(int radius) {
        Circle.radius = radius;
        if (radius <= 0) {
            throw new CircleException();
        }
    }
    @Override
    public String name() {
        return "Круг";
    }
    public static int circleLength() {
        return ICircleable.ICircleLength(radius);
    }
    @Override
    public int area() {
        return ICircleable.super.IArea(radius);
    }
}