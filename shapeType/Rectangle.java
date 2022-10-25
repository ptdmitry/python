package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.Shape;

public class Rectangle extends Shape {

    private final int length;
    private final int width;

    public Rectangle(int length, int width) {
        this.length = length;
        this.width = width;
    }

    @Override
    public String name() {
        return "Прямоугольник";
    }

    @Override
    public int area() {
        return length * width;
    }

    @Override
    public int perimeter() {
        return (length + width) * 2;
    }
}