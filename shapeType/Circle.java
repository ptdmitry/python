package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.Shape;

public class Circle extends Shape {

    private final int radius;

    public Circle(int radius) {
        this.radius = radius;
    }

    @Override
    public String name() {
        return "Круг";
    }

    @Override
    public int area() {
        return (int) (Math.PI * radius * radius);
    }

    @Override
    public int perimeter() {
        return 0;
    }

    @Override
    public int circleLength() {
        return (int) (2 * Math.PI * radius);
    }
}