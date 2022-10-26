package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.exceptions.CircleException;
import ArchitecturePO.Lesson3.Shape.interFaceAction.ICircleable;
import ArchitecturePO.Lesson3.Shape.interFaceAction.Shape;

public class Circle extends Shape implements ICircleable {
    private final int radius;

    public Circle(int radius) {
        this.radius = radius;
        if (radius <= 0) {
            throw new CircleException();
        }
    }
    @Override
    public String name() {
        return "Круг";
    }
    @Override
    public int circleLength() {
        return ICircleable.super.ICircleLength(radius);
    }
    @Override
    public int perimeter() {
        return 0;
    }
    @Override
    public int area() {
        return ICircleable.super.IArea(radius);
    }
}