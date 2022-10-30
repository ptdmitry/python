package ArchitecturePO.Lesson3.Shape.exceptions;

public class TriangleException extends RuntimeException {
    public TriangleException() {
        super("Треугольник не существует");
    }
}