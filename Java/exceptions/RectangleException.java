package ArchitecturePO.Lesson3.Shape.exceptions;

public class RectangleException extends RuntimeException {
    public RectangleException() {
        super("Прямоугольник не существует");
    }
}