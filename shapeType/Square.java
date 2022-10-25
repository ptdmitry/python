package ArchitecturePO.Lesson3.Shape.shapeType;

import ArchitecturePO.Lesson3.Shape.Shape;

public class Square extends Shape {
    private final int length;

    public Square(int length) {
        this.length = length;
    }

    @Override
    public String name() {
        return "Квадрат";
    }

    @Override
    public int area() {
        return length * length;
    }

    @Override
    public int perimeter() {
        return length * 4;
    }
}